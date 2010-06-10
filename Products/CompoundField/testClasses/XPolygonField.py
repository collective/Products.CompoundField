# -*- coding: utf-8 -*-
#
# File: XPolygonField.py
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

#XPolygonField

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
##/code-section module-header

from zope.interface import implements
from Products.CompoundField.testClasses.XPointField import XPointField
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.CompoundField.ArrayField import ArrayField
from Products.CompoundField.ArrayWidget import ArrayWidget
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget


from Products.CompoundField.CompoundField import CompoundField
######CompoundField
schema = Schema((

    ArrayField(
        XPointField(
            name='polypoints',
            widget=XPointField._properties['widget'](
                label='Polypoints',
                label_msgid='CompoundField_label_polypoints',
                i18n_domain='CompoundField',
            ),
        ),

        widget=EnhancedArrayWidget(
            label='Array:polypoints',
            label_msgid='CompoundField_label_array:polypoints',
            i18n_domain='CompoundField',
        ),
    ),

),
)




class XPolygonField(CompoundField):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header



    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'xpolygonfield',
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


registerField(XPolygonField,
              title='XPolygonField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



