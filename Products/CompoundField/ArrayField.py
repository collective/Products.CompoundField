# -*- coding: utf-8 -*-
#
# File: ArrayField.py
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

#ArrayField

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
from Products.Archetypes.Schema import Schema
from Products.CompoundField.validators import ArrayValidator
from types import DictType
from copy import deepcopy
##/code-section module-header

from zope.interface import implements
from Products.CompoundField.CompoundField import CompoundField
from Products.CompoundField.IArrayField import IArrayField
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin



from Products.CompoundField.CompoundField import CompoundField
######CompoundField
schema = Schema((


),
)




class ArrayField(CompoundField):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    implements(IArrayField)


    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'arrayfield',
        'widget':EnhancedArrayWidget,
        ##code-section field-properties #fill in your manual code here
        'validators': ArrayValidator(),
        'autoresize': False,
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()

    schema=schema

    security.declarePrivate('set')
    security.declarePrivate('get')

    def __init__(self, field, size=5, *a, **kw):
        self.args = a
        self.kwargs = kw
        self.field = field
        CompoundField.__init__(self, self.field.getName(),
                               *self.args, **self.kwargs)
        self.resize(size)

    def getRaw(self, instance, **kwargs):
        return CompoundField.getRaw(self, instance, **kwargs)

    def set(self, instance, value, **kwargs):
        """sets value and distribute to subfields"""
        # keep evil eval for BBB, but: its a security hole
        # disabled by default
        if config.EVIL_EVAL and type(value) in (type(''),type(u'')):
            #if the value comes as string eval it to a dict
            value = eval(value)

        if type(value) == DictType:
            return CompoundField.set(self, instance, value, **kwargs)

        if not value:
            return
        
        fields = self.Schema().fields()[1:self.getSize(instance)+1]
        if self.autoresize and len(fields) != len(value):
            self.resize(len(value), instance=instance)
            fields = self.Schema().fields()[1:self.getSize(instance)+1]
        for i, f in enumerate(fields):
            if i >= len(value):
                break
            f.set(instance, value[i], **kwargs)

    def get(self, instance, **kwargs):
        res=list()
        size = self.getSize(instance)
        for f in self.Schema().fields()[1:size + 1]:
            res.append(f.get(instance, **kwargs))
        return res

    def getSize(self, instance):
        lf = self.Schema().fields()[0] #field 0 is always size. has to be adressed by index because fields get renamed during nesting

        size = lf.get(instance)
        if size is None:
            size = self.size

        if size > self.getPhysicalSize():
            self.resize(size, instance)

        return size

    def getPhysicalSize(self):
        """ returns the physical amount of subfields"""
        return getattr(self, 'physicalSize', 0)

    def copy(self):
        """
        Return a copy of field instance, consisting of field name and
        properties dictionary.
        """

        cdict = dict(vars(self))
        # Widget must be copied separatedly
        widget = cdict['widget']
        del cdict['widget']
        del cdict['schema']
        del cdict['field']
        properties = deepcopy(cdict)
        properties['widget'] = widget.copy()
        res = self.__class__(self.field, **properties)
        res.schema = self.Schema().copy()

        return res

    def resize(self, size, instance=None):
        oldsize = self.getPhysicalSize()

        #only do a physical resize when growing
        if size > oldsize or size==0 and oldsize==0:
            self.already_bootstrapped = False
            schema = Schema(())
            schema.addField(IntegerField('size'))
            fn = self.field.getName()

            for idx in range(max(size, 1)):
                f1 = self.field.copy()
                f1.__name__ = '%s%s%03d' % (fn, 
                                            config.ARRAY_FIELDNAME_SEPARATOR, 
                                            idx)
                schema.addField(f1)

            self.setSchema(schema=schema)
            self.physicalSize = size

        if instance:
            # field 0 is always size. has to be adressed by index because fields 
            # get renamed during nesting
            lf = self.Schema().fields()[0] 
            lf.set(instance, size)
            # We need to force a bootstrapping of the accessors by calling
            # getAccessor. There was a strange bug:
            # After a restart the content of an array field with a size
            # greater than default was not shown until after
            # a reload. Apparently the accessors was accessed
            # before the resize triggered by getSize().
            self.getAccessor(instance)
        else:
            self.size = size
    
    def fieldSeparator(self):
        return config.ARRAY_FIELDNAME_SEPARATOR
    
    def validate_required(self, instance, value, errors):
        request = instance.REQUEST
        sizekey = '%s%ssize' % (self.getName(), config.COMPOUND_FIELD_SEPERATOR)
        if sizekey in request and int(request[sizekey]) == 0:
            return Field.validate_required(self, instance, None, errors)
        else:
            return None
    
registerField(ArrayField,
              title='ArrayField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



