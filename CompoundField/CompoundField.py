# File: CompoundField.py
#
# Copyright (c) 2006 by eduplone Open Source Business Network EEIG
# Generator: ArchGenXML Version 1.5.0 svn/devel
#            http://plone.org/products/archgenxml
#
# German Free Software License (D-FSL)
#
# This Program may be used by anyone in accordance with the terms of the
# German Free Software License
# The License may be obtained under <http://www.d-fsl.org>.
#

__author__ = """Phil Auersperg <phil@bluedynamics.com>, Jens Klein
<jens.klein@jensquadrat.com>"""
__docformat__ = 'plaintext'

#CompoundField

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Field import ObjectField,encode,decode
from Products.Archetypes.Registry import registerField
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.Archetypes.Field  import *
from Products.Archetypes.Schema import Schema
try:
    from Products.generator import i18n
except ImportError:
    from Products.Archetypes.generator import i18n

from Products.CompoundField import config
from Products.CompoundField import utils

##code-section module-header #fill in your manual code here
import types
from Products.Archetypes.Schema import *
from Products.CompoundField import ClassGen
ListTypes = (types.TupleType, types.ListType)

#uugh, we need a special generator for the subfields

##/code-section module-header

from Products.CompoundField.ICompoundField import ICompoundField
from Products.CompoundField.IArrayField import IArrayField
from Products.CompoundField.CompoundWidget import CompoundWidget




class CompoundField(ObjectField):
    """
    """
    ##code-section class-header #fill in your manual code here
    security  = ClassSecurityInfo()
    schema=Schema(())
    ##/code-section class-header

    __implements__ = (getattr(ObjectField,'__implements__',()),) + (ICompoundField,)


    _properties = ObjectField._properties.copy()
    _properties.update({
        'type': 'compoundfield',
        'widget': CompoundWidget,
        'separator': '@@',
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()

    #from Interface ICompoundField:
    def Schema(self,):
        """Returns the Schemata for the CompoundField
        """
        return self.schema

    def getRaw(self, instance, **kwargs):
        res={}
        for f in self.Schema().fields():
            res[f.old_name]=(f.getRaw(instance,schema=self.schema))

        return res

    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        #print 'COMPOUNDFIELD:SET:',value
        #import pdb;pdb.set_trace()
        if not value:
            return

        if type(value) in types.StringTypes:
            #if the value comes as string eval it to a dict
            # XXX attention: use restricted environment instead!
            # this is a potential security hole.
            # reval function should fix this in 90% case
            value = utils.reval(value)

        if getattr(self, 'value_class', None):
            if isinstance(value, self.value_class):
                value = self.valueClass2Raw(value)

        for f in self.Schema().fields():
            if value.has_key(f.old_name):
                v = value[f.old_name]
                isarray = type(v) in ListTypes and \
                          len(v)==2 and \
                          type(v[1]) == types.DictType
                if v and isarray:
                    kw=v[1]
                else:
                    kw={}

                if v:
                    if isarray or (type(v) in ListTypes and len(v) ==1):
                        f.set(instance, v[0], **kw)
                    else:
                        f.set(instance, v, **kw)

    security.declarePrivate('get')
    def get(self, instance, **kwargs):
        """ get

        Why it is private ?
        why it returns a dictionnary ?
        """
        res={}
        for f in self.getFields():
            res[f.old_name]=f.get(instance)

        if getattr(self,'value_class',None):
            res=self.raw2ValueClass(res)

        return res

    security.declarePublic('getField')
    def getField(self, fieldname):
        """Return internal compound field
        """
        for field in self.getFields():
            if field.old_name == fieldname:
                return field

        return None

    def raw2ValueClass(self,dict):
        res=self.value_class()
        res.__dict__.update(dict)
        return res

    def setSchema(self, schema):
        self.schema = schema
        self.calcFieldNames()

    def calcFieldNames(self, path=[]):
        """ prefixes the field names with the parent field name """

        _fields = self.Schema()._fields

        for f in self.Schema().fields():
            old_name = f.getName()
            if ICompoundField.isImplementedBy(f):
                f.calcFieldNames(path=path+[self])

            if not getattr(f, 'prefixed', False):
                f.old_name = f.getName()
                f.prefixed = True

            f.__name__ = self.separator.join([getattr(field, 'old_name', field.getName())
                                              for field in path+[self]+[f]])
            #del _fields[old_name]
            _fields[f.__name__]=f

    def getAccessor(self, instance):
        """ hook to post-generate the accessors for the subfields
            its a little bit hacky, because we need a special ClassGen here
        """

        if not getattr(self,'already_bootstrapped',False):
            fields=self.getFields()
            ClassGen.generateMethods(instance.__class__,self.Schema())
            self.already_bootstrapped=True
        return ObjectField.getAccessor(self,instance)

    def __init__(self, name=None, schema=None, **kwargs):
        ObjectField.__init__(self, name, **kwargs)

        if not schema:
            schema=self.schema.copy()

        self.setSchema(schema)

    security.declarePublic('getFields')
    def getFields(self,):
        return self.Schema().fields()

    def valueClass2Raw(self,value):
        res={}
        for k in value.__dict__:
            res[k]=(getattr(value,k),)

        return res

registerField(CompoundField,
              title='CompoundField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



