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
        'widget':ArrayWidget,
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()

    schema=schema

    security.declarePrivate('set')
    security.declarePrivate('get')


    def getRaw(self, instance, **kwargs):
        return CompoundField.getRaw(self,instance,**kwargs)

    def set(self, instance, value, **kwargs):
        #print 'Arrayfield:set: %s' % value
        #import pdb;pdb.set_trace()
        if type(value) in (type(''),type(u'')):
            #if the value comes as string eval it to a dict
            value=eval(value)

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

    def get(self, instance, **kwargs):
        res=[]
        for f in self.Schema().fields()[1:self.getSize(instance)+1]:
            res.append(f.get(instance))

        return res

    def getSize(self,instance=None):
        if instance:
            lf=self.Schema().fields()[0] #field 0 is always size. has to be adressed by index because fields get renamed during nesting

            size=lf.get(instance)
            if size is None:
                size=self.size

            if size > self.getPhysicalSize():
                self.resize(size,instance)

            return size
        else:
            return self.size

    def __init__(self,field,size=5,*a,**kw):

        self.args=a
        self.kwargs=kw
        self.field=field
        CompoundField.__init__(self,self.field.getName(),*self.args,**self.kwargs)
        self.resize(size)

    def getPhysicalSize(self):
        """ returns the physical amount of subfields"""
        return getattr(self,'physicalSize',0)

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
        res=self.__class__(self.field,**properties)
        res.schema=self.Schema().copy()

        return res

    def resize(self, size, instance=None):

        oldsize=self.getPhysicalSize()

        #only do a physical resize when growing
        if size>oldsize:
            self.already_bootstrapped=False
            schema=Schema(())
            schema.addField(IntegerField('size'))
            fn=self.field.getName()

            for i in range(size):
                f1=self.field.copy()
                f1.__name__='%s:%03d' % (fn,i)
                schema.addField(f1)

            self.setSchema(schema=schema)
            self.physicalSize=size

        if instance:
            lf=self.Schema()['size']
            lf.set(instance,size)
        else:
            self.size=size


registerField(ArrayField,
              title='ArrayField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



