#overloaded classgen version to handle schemas within fields

from __future__ import nested_scopes
import re
from types import FunctionType as function

from Products.Archetypes.utils import capitalize
from Products.Archetypes.utils import _getSecurity
from Products.Archetypes.debug import warn
from Products.Archetypes.debug import deprecated
from Acquisition import ImplicitAcquisitionWrapper
from AccessControl import ClassSecurityInfo
from Globals import InitializeClass

from Products.Archetypes import ClassGen
# marker that AT should generate a method -- used to discard unwanted
#  inherited methods
AT_GENERATE_METHOD = []


_modes = {
    'r' : { 'prefix'   : 'get',
            'attr'     : 'accessor',
            'security' : 'read_permission',
            },
    'm' : { 'prefix'   : 'getRaw',
            'attr'     : 'edit_accessor',
            'security' : 'write_permission',
            },
    'w' : { 'prefix'   : 'set',
            'attr'     : 'mutator',
            'security' : 'write_permission',
            },

    }


class Generator(ClassGen.Generator):

    def makeMethod(self, klass, field, mode, methodName,schema):
        name = field.getName()
        method = None
        if mode == "r":
            def generatedAccessor(self, **kw):
                """Default Accessor."""
                return schema[name].get(self, **kw)
            method = generatedAccessor
        elif mode == "m":
            def generatedEditAccessor(self, **kw):
                """Default Edit Accessor."""
                try:
                    return schema[name].getRaw(self, **kw)
                except:
                    print 'kw:',kw
                    raise
                    
            method = generatedEditAccessor
        elif mode == "w":
            def generatedMutator(self, value, **kw):
                """Default Mutator."""
                return schema[name].set(self, value, **kw)
            method = generatedMutator
        else:
            raise GeneratorError("""Unhandled mode for method creation:
            %s:%s -> %s:%s""" %(klass.__name__,
                                name,
                                methodName,
                                mode))

        # Zope security requires all security protected methods to have a
        # function name. It uses this name to determine which roles are allowed
        # to access the method.
        # This code is renaming the internal name from e.g. generatedAccessor to
        # methodName.
        method = function(method.func_code,
                          method.func_globals,
                          methodName,
                          method.func_defaults,
                          method.func_closure,
                         )
        setattr(klass, methodName, method)

class ClassGenerator(ClassGen.ClassGenerator):

    def generateMethods(self, klass, schema):
        generator = Generator()
        fields=schema.fields()
        for field in fields:
            assert not 'm' in field.mode, 'm is an implicit mode'

            # Make sure we want to muck with the class for this field
            if "c" not in field.generateMode: continue
            type = getattr(klass, 'type')
            for mode in field.mode: #(r, w)
                self.handle_mode(klass, generator, type, field, mode, schema)
                if mode == 'w':
                    self.handle_mode(klass, generator, type, field, 'm', schema)

        InitializeClass(klass)

    def handle_mode(self, klass, generator, type, field, mode, schema):
        attr = _modes[mode]['attr']
        # Did the field request a specific method name?
        methodName = getattr(field, attr, None)
        if not methodName:
            methodName = generator.computeMethodName(field, mode)

        # Avoid name space conflicts
        if not hasattr(klass, methodName) \
               or getattr(klass, methodName) is AT_GENERATE_METHOD:
            if type.has_key(methodName):
                raise GeneratorError("There is a conflict"
                                     "between the Field(%s) and the attempt"
                                     "to generate a method of the same name on"
                                     "class %s" % (
                    methodName,
                    klass.__name__))


            # Make a method for this klass/field/mode
            generator.makeMethod(klass, field, mode, methodName, schema)

        # Update security regardless of the method being generated or
        # not. Not protecting the method by the permission defined on
        # the field may leave security open and lead to misleading
        # bugs.
        self.updateSecurity(klass, field, mode, methodName)

        # Note on the class what we did (even if the method existed)
        attr = _modes[mode]['attr']
        setattr(field, attr, methodName)

_cg = ClassGenerator()
generateClass = _cg.generateClass
generateMethods = _cg.generateMethods
