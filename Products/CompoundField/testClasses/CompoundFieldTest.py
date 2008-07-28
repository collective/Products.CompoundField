# -*- coding: utf-8 -*-
#
# File: CompoundFieldTest.py
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
from Products.CompoundField.CompoundField import CompoundField
from Products.CompoundField.testClasses.XBoxField import XBoxField
from Products.CompoundField.testClasses.XPointField import XPointField
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.CompoundField.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    CompoundField(
        name='point',
        widget=CompoundField._properties['widget'](
            label='Point',
            label_msgid='CompoundField_label_point',
            i18n_domain='CompoundField',
        ),
        schema=Schema((IntegerField('x'),IntegerField('y'))),
    ),
    XBoxField(
        name='box',
        widget=XBoxField._properties['widget'](
            label='Box',
            label_msgid='CompoundField_label_box',
            i18n_domain='CompoundField',
        ),
    ),
    XPointField(
        name='point2',
        widget=XPointField._properties['widget'](
            label='Point2',
            label_msgid='CompoundField_label_point2',
            i18n_domain='CompoundField',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CompoundFieldTest_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CompoundFieldTest(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.ICompoundFieldTest)

    meta_type = 'CompoundFieldTest'
    _at_rename_after_creation = True

    schema = CompoundFieldTest_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(CompoundFieldTest, PROJECTNAME)
# end of class CompoundFieldTest

##code-section module-footer #fill in your manual code here
##/code-section module-footer



