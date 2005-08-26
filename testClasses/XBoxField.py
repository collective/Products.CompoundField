# File: XBoxField.py
# 
# Copyright (c) 2005 by eduplone Open Source Business Network EEIG
# Generator: ArchGenXML Version 1.4.0-beta2 devel 
#            http://plone.org/products/archgenxml
#
# This software is released under the German Free Software License (D-FSL).
# The full text of this license is delivered with this product or is available
# at http://www.dipp.nrw.de/d-fsl
#
__author__  = '''Phil Auersperg <phil@bluedynamics.com>, Jens Klein
<jens.klein@jensquadrat.com>'''
__docformat__ = 'plaintext'

from types import ListType, TupleType, StringTypes
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
from Products.generator import i18n

from Products.CompoundField import config

##code-section module-header #fill in your manual code here
##/code-section module-header

from XPointField import XPointField
from XBox import XBox


from Products.CompoundField.CompoundField import CompoundField
######CompoundField
schema=Schema((
    XPointField('p1',
    
    ),
    
    XPointField('p2',
    
    ),
    
),
)



class XBoxField(CompoundField):
    ''' '''

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(CompoundField,'__implements__',()),)


    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'xboxfield',
        'value_class':XBox,
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
        return CompoundField.set(self,instance,value,**kwargs)
                        
    def get(self, instance, **kwargs):
        return CompoundField.get(self,instance,**kwargs)
                        

registerField(XBoxField,
              title='XBoxField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



