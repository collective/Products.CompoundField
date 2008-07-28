# -*- coding: utf-8 -*-
#
# File: NestedArrayFieldTest.py
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
from Products.CompoundField.testClasses.NestedArrayField import NestedArrayField
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
        NestedArrayField(
            name='nestedArray',
            widget=NestedArrayField._properties['widget'](
                label='Nestedarray',
                label_msgid='CompoundField_label_nestedArray',
                i18n_domain='CompoundField',
            ),
        ),

        widget=EnhancedArrayWidget(
            label='Array:nestedarray',
            label_msgid='CompoundField_label_array:nestedArray',
            i18n_domain='CompoundField',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

NestedArrayFieldTest_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class NestedArrayFieldTest(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.INestedArrayFieldTest)

    meta_type = 'NestedArrayFieldTest'
    _at_rename_after_creation = True

    schema = NestedArrayFieldTest_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(NestedArrayFieldTest, PROJECTNAME)
# end of class NestedArrayFieldTest

##code-section module-footer #fill in your manual code here
##/code-section module-footer



