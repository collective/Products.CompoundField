# -*- coding: utf-8 -*-
#
# File: XBoxField.py
#
# Copyright (c) 2007 by BlueDynamics Alliance, 2005-2006 by eduplone Open
# Source Business Network EEIG
# Generator: ArchGenXML Version 1.5.3 dev/svn
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

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.Field import ObjectField, encode, decode
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
from Products.CompoundField.testClasses.XPointField import XPointField
from Products.CompoundField.testClasses.XBox import XBox


from Products.CompoundField.CompoundField import CompoundField
schema = Schema((

    XPointField(
        name='p1',
        widget=XPointField._properties['widget'](
            label='P1',
            label_msgid='CompoundField_label_p1',
            i18n_domain='CompoundField',
        )
    ),

    XPointField(
        name='p2',
        widget=XPointField._properties['widget'](
            label='P2',
            label_msgid='CompoundField_label_p2',
            i18n_domain='CompoundField',
        )
    ),

),
)


##code-section module-header #fill in your manual code here
##/code-section module-header


class XBoxField(CompoundField):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(CompoundField,'__implements__',()),)


    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'xboxfield',
        'value_class': XBox,
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })
        
    schema = schema
    security  = ClassSecurityInfo()
    ##code-section security-declarations #fill in your manual code here
    ##/code-section security-declarations

    security.declarePrivate('get')
    security.declarePrivate('getRaw')
    security.declarePrivate('set')

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



