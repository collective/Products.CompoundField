# File: ArrayField.py
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
try:
    from Products.generator import i18n
except ImportError:
    from Products.Archetypes.generator import i18n

from Products.CompoundField import config
from Products.CompoundField import utils

##code-section module-header #fill in your manual code here
from Products.Archetypes.Schema import Schema
from types import DictType
from copy import deepcopy
##/code-section module-header

from Products.CompoundField.CompoundField import CompoundField
from Products.CompoundField.IArrayField import IArrayField
from Products.CompoundField.ArrayWidget import ArrayWidget


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

    __implements__ = (getattr(CompoundField,'__implements__',()),) + \
                     (getattr(CompoundField,'__implements__',()),) + \
                     (IArrayField,)


    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'arrayfield',
        'widget': ArrayWidget,
        'separator': '$'
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()

    schema=schema

    def getRaw(self, instance, **kwargs):
        return CompoundField.getRaw(self,instance,**kwargs)

    security.declarePrivate('set')
    def set(self, instance, value, **kwargs):
        #print 'Arrayfield:set: %s' % value
        #import pdb;pdb.set_trace()
        if type(value) in (type(''),type(u'')):
            #if the value comes as string eval it to a dict
            # XXX attention: use restricted environment instead!
            # this is a potential security hole.
            # reval function should fix this in 90% case
            value = utils.reval(value)

        if type(value)==DictType:
            return CompoundField.set(self,instance,value,**kwargs)

        if not value:
            return
        i=0
        for f in self.Schema().fields()[1:self.getSize(instance)+1]:
            if i>=len(value):
                break

            f.set(instance,value[i],**kwargs)
            i+=1

    security.declarePrivate('get')
    def get(self, instance, **kwargs):
        res=[]
        for f in self.Schema().fields()[1:]:
            res.append(f.get(instance))

        return res

    def getSize(self, instance=None):
        self.size = self.getPhysicalSize()
        return self.size

    def __init__(self,field,size=5,*a,**kw):

        self.args=a
        self.kwargs=kw
        self.field=field
        CompoundField.__init__(self,self.field.getName(),*self.args,**self.kwargs)
        self.resize(size)

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
        if cdict.has_key('kwargs'):
            del cdict['kwargs']
        properties = deepcopy(cdict)
        properties['widget'] = widget.copy()
        res=self.__class__(self.field,**properties)
        res.schema=self.Schema().copy()

        return res

    def fieldCopy(self, field):
        """Replacement of field.copy() for Zope < 2.8

        The code from Archetypes.Fields.py copy() adapted for us.
        """
        cdict = dict(vars(field))
        # Widget and schema must be copied separatedly
        widget = cdict['widget']
        del cdict['widget']
        schema = None
        if cdict.has_key('schema'):
            schema = cdict['schema']
            del cdict['schema']

        properties = deepcopy(cdict)

        properties['widget'] = widget.copy()
        if schema:
            # This one must fail too, but we never know...
            try:
                properties['schema'] = schema.copy()
            except TypeError:
                c = Schemata()
                for subfield in schema.fields():
                    c.addField(self.fieldCopy(subfield))
                properties['schema'] = c

        return field.__class__(self.field.getName(), **properties)

    def resize(self, size, instance=None):
        oldsize=self.getPhysicalSize()

        if size == oldsize:
            return

        #only do a physical resize when growing
        else:

            self.already_bootstrapped = False
            schema = Schema(())
            schema.addField(IntegerField('size'))

            fieldname = self.field.getName()

            for i in range(size):
                try:
                    f1 = self.field.copy()
                except TypeError:
                    # Zope < 2.8 fallback
                    f1 = self.fieldCopy(self.field)

                f1.__name__ = '%s%s%03d' % (fieldname, self.separator, i)
                schema.addField(f1)

            self.setSchema(schema=schema)
            self.physicalSize = size


        if instance:
            # field 0 is always size. has to be adressed by index because fields
            # get renamed during nesting
            field = self.Schema().fields()[0]
            field.set(instance, size)
        else:
            self.size = size



registerField(ArrayField,
              title='ArrayField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



