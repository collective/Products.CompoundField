# -*- coding: utf-8 -*-
#
# File: ArrayFieldTest.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces
from Products.CompoundField.ArrayField import ArrayField
from Products.CompoundField.testClasses.XPolygonField import XPolygonField
from Products.CompoundField.testClasses.XBoxField import XBoxField
from Products.CompoundField.testClasses.XPointField import XPointField
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.CompoundField.ArrayField import ArrayField
from Products.CompoundField.ArrayWidget import ArrayWidget
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget
from Products.CompoundField.EnhancedArrayWidget import EnhancedArrayWidget
from Products.CompoundField.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ArrayField(
        StringField(
            name='names',
            widget=StringField._properties['widget'](
                label='Names',
                label_msgid='CompoundField_label_names',
                i18n_domain='CompoundField',
            ),
        ),

        widget=EnhancedArrayWidget(
            label='Array:names',
            label_msgid='CompoundField_label_array:names',
            i18n_domain='CompoundField',
        ),
    ),
    ArrayField(
        XPointField(
            name='points',
            widget=XPointField._properties['widget'](
                label='Points',
                label_msgid='CompoundField_label_points',
                i18n_domain='CompoundField',
            ),
        ),

        widget=EnhancedArrayWidget(
            label='Array:points',
            label_msgid='CompoundField_label_array:points',
            i18n_domain='CompoundField',
        ),
    ),
    ArrayField(
        XBoxField(
            name='boxes',
            widget=XBoxField._properties['widget'](
                label='Boxes',
                label_msgid='CompoundField_label_boxes',
                i18n_domain='CompoundField',
            ),
        ),

        widget=EnhancedArrayWidget(
            label='Array:boxes',
            label_msgid='CompoundField_label_array:boxes',
            i18n_domain='CompoundField',
        ),
    ),
    XPolygonField(
        name='points1',
        widget=XPolygonField._properties['widget'](
            label='Points1',
            label_msgid='CompoundField_label_points1',
            i18n_domain='CompoundField',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ArrayFieldTest_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ArrayFieldTest(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IArrayFieldTest)

    meta_type = 'ArrayFieldTest'
    _at_rename_after_creation = True

    schema = ArrayFieldTest_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def testset(self, value):
        self.Schema()['names'].fields()[1].set(self,value)



registerType(ArrayFieldTest, PROJECTNAME)
# end of class ArrayFieldTest

##code-section module-footer #fill in your manual code here
##/code-section module-footer



