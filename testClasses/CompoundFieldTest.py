# File: CompoundFieldTest.py
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

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *

from Products.CompoundField.CompoundField import CompoundField
from XPointField import XPointField


from Products.CompoundField.config import *
##code-section module-header #fill in your manual code here
##/code-section module-header

schema=Schema((
    CompoundField('point',
        schema=Schema((IntegerField('x'),IntegerField('y')))
    ),
    
    CompoundField('box',
    
    ),
    
    XPointField('point2',
    
    ),
    
),
)


##code-section after-schema #fill in your manual code here

schema['box'].setSchema(Schema((
            CompoundField(
                'point1',
                schema=Schema(
                    (IntegerField('x'),
                    IntegerField('y')
                    
                    ))),
                    
            CompoundField(
                'point2',
                schema=Schema(
                    (IntegerField('x'),
                    IntegerField('y')
                    
                    ))),
            )))
##/code-section after-schema

class CompoundFieldTest(BaseContent):
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)


    # This name appears in the 'add' box
    archetype_name             = 'CompoundFieldTest'

    meta_type                  = 'CompoundFieldTest' 
    portal_type                = 'CompoundFieldTest' 
    allowed_content_types      = [] 
    filter_content_types       = 0
    global_allow               = 0
    allow_discussion           = 0
    #content_icon               = 'CompoundFieldTest.gif'
    immediate_view             = 'base_view'
    default_view               = 'base_view'
    typeDescription            = "CompoundFieldTest"
    typeDescMsgId              = 'description_edit_compoundfieldtest'

    schema = BaseSchema + \
             schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    #Methods

registerType(CompoundFieldTest,PROJECTNAME)
# end of class CompoundFieldTest

##code-section module-footer #fill in your manual code here
##/code-section module-footer



