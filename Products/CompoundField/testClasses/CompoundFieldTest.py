# -*- coding: utf-8 -*-
#
# File: CompoundFieldTest.py
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
<jens@bluedynamics.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.CompoundField.CompoundField import CompoundField
from Products.CompoundField.testClasses.XBoxField import XBoxField
from Products.CompoundField.testClasses.XPointField import XPointField
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
        schema=Schema((IntegerField('x'),IntegerField('y')))
    ),

    XBoxField(
        name='box',
        widget=XBoxField._properties['widget'](
            label='Box',
            label_msgid='CompoundField_label_box',
            i18n_domain='CompoundField',
        )
    ),

    XPointField(
        name='point2',
        widget=XPointField._properties['widget'](
            label='Point2',
            label_msgid='CompoundField_label_point2',
            i18n_domain='CompoundField',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

CompoundFieldTest_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class CompoundFieldTest(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'CompoundFieldTest'

    meta_type = 'CompoundFieldTest'
    portal_type = 'CompoundFieldTest'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 0
    #content_icon = 'CompoundFieldTest.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "CompoundFieldTest"
    typeDescMsgId = 'description_edit_compoundfieldtest'

    _at_rename_after_creation = True

    schema = CompoundFieldTest_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(CompoundFieldTest, PROJECTNAME)
# end of class CompoundFieldTest

##code-section module-footer #fill in your manual code here
##/code-section module-footer



