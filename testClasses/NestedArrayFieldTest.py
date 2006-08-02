# -*- coding: utf-8 -*-
#
# File: NestedArrayFieldTest.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from Products.CompoundField.testClasses.NestedArrayField import NestedArrayField
from Products.CompoundField.ArrayField import ArrayField
from Products.CompoundField.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

ArrayField(            NestedArrayField(
                name='nestedArray',
            
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

class NestedArrayFieldTest(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'NestedArrayFieldTest'

    meta_type = 'NestedArrayFieldTest'
    portal_type = 'NestedArrayFieldTest'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'NestedArrayFieldTest.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "NestedArrayFieldTest"
    typeDescMsgId = 'description_edit_nestedarrayfieldtest'

    _at_rename_after_creation = True

    schema = NestedArrayFieldTest_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(NestedArrayFieldTest, PROJECTNAME)
# end of class NestedArrayFieldTest

##code-section module-footer #fill in your manual code here
##/code-section module-footer



