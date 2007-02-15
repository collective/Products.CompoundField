# -*- coding: utf-8 -*-
#
# File: ArrayFieldTest.py
#
# Copyright (c) 2007 by eduplone Open Source Business Network EEIG (2005-2006),
# BlueDynamics Alliance
# Generator: ArchGenXML Version 1.5.2
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
from Products.CompoundField.ArrayField import ArrayField
from Products.CompoundField.testClasses.XPolygonField import XPolygonField
from Products.CompoundField.testClasses.XBoxField import XBoxField
from Products.CompoundField.testClasses.XPointField import XPointField
from Products.CompoundField.ArrayField import ArrayField
from Products.CompoundField.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ArrayField(
        StringField(
                name='names',
                widget=StringWidget(
                    label='Names',
                    label_msgid='CompoundField_label_names',
                    i18n_domain='CompoundField',
                )
            ),
        
    ),

    ArrayField(
        XPointField(
                name='points',
                widget=XPointField._properties['widget'](
                    label='Points',
                    label_msgid='CompoundField_label_points',
                    i18n_domain='CompoundField',
                )
            ),
        
    ),

    ArrayField(
        XBoxField(
                name='boxes',
                widget=XBoxField._properties['widget'](
                    label='Boxes',
                    label_msgid='CompoundField_label_boxes',
                    i18n_domain='CompoundField',
                )
            ),
        
    ),

    XPolygonField(
        name='points1',
        widget=XPolygonField._properties['widget'](
            label='Points1',
            label_msgid='CompoundField_label_points1',
            i18n_domain='CompoundField',
        )
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ArrayFieldTest_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ArrayFieldTest(BaseContent):
    """
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'ArrayFieldTest'

    meta_type = 'ArrayFieldTest'
    portal_type = 'ArrayFieldTest'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'ArrayFieldTest.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "ArrayFieldTest"
    typeDescMsgId = 'description_edit_arrayfieldtest'


    actions =  (


       {'action': "string:${object_url}/arrayfield_test",
        'category': "object",
        'id': 'arrayfield_test',
        'name': 'arrayfield_test',
        'permissions': ("View",),
        'condition': 'python:1'
       },


    )

    _at_rename_after_creation = True

    schema = ArrayFieldTest_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def testset(self, value):
        import pdb;pdb.set_trace()
        self.Schema()['names'].fields()[1].set(self,value)



registerType(ArrayFieldTest, PROJECTNAME)
# end of class ArrayFieldTest

##code-section module-footer #fill in your manual code here
##/code-section module-footer



