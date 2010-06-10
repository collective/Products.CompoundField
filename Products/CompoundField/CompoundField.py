# -*- coding: utf-8 -*-
#
# File: CompoundField.py
#
# Copyright (c) 2008 by BlueDynamics Alliance (since 2007), 2005-2006 by
# eduplone Open Source Business Network EEIG
# Generator: ArchGenXML Version 2.2 (svn)
#            http://plone.org/products/archgenxml
#
# German Free Software License (D-FSL)
#

__author__ = """Phil Auersperg <phil@bluedynamics.com>, Jens Klein <jens@bluedynamics.com>"""
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

from Products.CompoundField import config

##code-section module-header #fill in your manual code here
import types
from Products.Archetypes.Schema import *
from Products.CompoundField import ClassGen
from Products.CompoundField.validators import CompoundValidator
ListTypes = (types.TupleType, types.ListType)

#uugh, we need a special generator for the subfields

##/code-section module-header

from zope.interface import implements
from Products.CompoundField.ICompoundField import ICompoundField
from Products.CompoundField.CompoundWidget import CompoundWidget
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin





class CompoundField(ObjectField):
    """
    """
    ##code-section class-header #fill in your manual code here
    security  = ClassSecurityInfo()
    security.declarePublic('getFields')
    schema=Schema(())
    ##/code-section class-header

    implements(ICompoundField)


    _properties = ObjectField._properties.copy()
    _properties.update({
        'type': 'compoundfield',
        'widget': CompoundWidget,
        'validators': CompoundValidator(),
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()


    security.declarePrivate('set')
    security.declarePrivate('get')


    #from Interface ICompoundField:
    def Schema(self,):
        """Returns the Schemata for the CompoundField
        """
        return self.schema

    def getRaw(self, instance, **kwargs):
        res = dict()
        for f in self.Schema().fields():
            res[f.old_name] = (f.getRaw(instance, schema=self.schema))
        return res

    def set(self, instance, value, **kwargs):
        if not value:
            return
            
        # keep evil eval for BBB, but: its a security hole
        # disabled by default
        if config.EVIL_EVAL and type(value) in types.StringTypes:
            #if the value comes as string eval it to a dict
            # XXX attention: use restricted environment instead!
            # this is a potential security hole.
            value = eval(value)

        if getattr(self, 'value_class', None):
            if isinstance(value, self.value_class):
                value = self.valueClass2Raw(value)

        for f in self.Schema().fields():
            if value.has_key(f.old_name):
                v = value[f.old_name]
                isarray = type(v) in ListTypes and len(v)==2 and type(v[1]) == types.DictType
                if v and isarray:
                    kw=v[1]
                else:
                    kw={}
                
                request = instance.REQUEST
                if (v or \
                    f.type == 'lines' and \
                    not ('controller_state' in request and \
                         request['controller_state'].getErrors())):
                    if isarray or (type(v) in ListTypes and len(v) ==1) and f.type != 'datagrid':
                        f.set(instance, v[0], **kw)
                    else:
                        f.set(instance, v, **kw)

    def get(self, instance, **kwargs):
        res = dict()
        for field in self.Schema().fields():
            res[field.old_name] = field.get(instance,**kwargs)
        if getattr(self, 'value_class', None):
            res = self.raw2ValueClass(res)
        return res

    def raw2ValueClass(self,dict):
        res = self.value_class()
        res.__dict__.update(dict)
        return res

    def setSchema(self, schema):
        self.schema = schema
        self.calcFieldNames()

    def calcFieldNames(self, path = [], force_prefix = False):
        ''' prefixes the field names with the parent field name '''
        _fields = self.Schema()._fields

        for f in self.Schema().fields():
            if not getattr(f, 'prefixed', False) or force_prefix:
                # calcFieldNames are often called several times for the same
                # field, e.g. when copying a schema. We do not want to perform
                # prefixing everytime this method is called. We only want to
                # prefix field names in two cases:
                # a) The first time we process a field
                # b) If calcFieldNames is called recursively on subfields, to
                # apply the correct parent field names to the prefixing of a
                # subfield. In this case we set the paramter force_prefix.
                if not getattr(f, 'prefixed', False):
                    # only set old_name the first time we prefix a field - old_name
                    # is the original field name, that we want to use in all prefixings of a field.
                    f.old_name =  f.getName()
                    f.prefixed = 1
                f.__name__ = config.COMPOUND_FIELD_SEPERATOR.join(
                    [getattr(field, 'old_name', field.getName()) for field in path + [self] + [f]])
                #del _fields[old_name]
                _fields[f.__name__] = f
                if ICompoundField.providedBy(f):
                    f.calcFieldNames(path = path + [self], force_prefix = True)

    def getAccessor(self, instance):
        ''' hook to post-generate the accessors for the subfields
            its a little bit hacky, because we need a special ClassGen here
        '''
        if not getattr(self, 'already_bootstrapped', False):
            fields = self.getFields()
            ClassGen.generateMethods(instance.__class__, self.Schema())
            self.already_bootstrapped = True
        return ObjectField.getAccessor(self, instance)

    def valueClass2Raw(self,value):
        res = dict()
        for k in value.__dict__:
            res[k]=(getattr(value, k),)
        return res

    def getFields(self,):
        return self.Schema().fields()

    def getField(self, key):
        """ get subfield of @param key"""
        return self.Schema().get(key)
    
    def __init__(self, name=None, schema=None, **kwargs):
        ObjectField.__init__(self, name, **kwargs)
        if not schema:
            schema = self.schema.copy()
        self.setSchema(schema)


registerField(CompoundField,
              title='CompoundField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer
