# File: ArrayFieldTest.py
# 
# Copyright (c) 2005 by eduplone Open Source Business Network EEIG
# Generator: ArchGenXML Version 1.4.0-RC1 devel 
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
from Products.CompoundField.ArrayField import ArrayField
from XPolygonField import XPolygonField
from XBoxField import XBoxField
from XPointField import XPointField
from Products.CompoundField.ArrayField import ArrayField


from Products.CompoundField.config import *
##code-section module-header #fill in your manual code here
##/code-section module-header

schema=Schema((
ArrayField(        StringField('names',
            widget=StringWidget(
                label='Names',
                label_msgid='CompoundField_label_names',
                description_msgid='CompoundField_help_names',
                i18n_domain='CompoundField',
            )
        ),
    ),
ArrayField(        XPointField('points',
        
        ),
    ),
ArrayField(        XBoxField('boxes',
        
        ),
    ),
    XPolygonField('points1',
    
    ),

),
)


##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

ArrayFieldTest_schema = BaseSchema + \
    schema

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class ArrayFieldTest(BaseContent):
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)


    # This name appears in the 'add' box
    archetype_name             = 'ArrayFieldTest'

    meta_type                  = 'ArrayFieldTest'
    portal_type                = 'ArrayFieldTest'
    allowed_content_types      = []
    filter_content_types       = 0
    global_allow               = 1
    allow_discussion           = 0
    #content_icon               = 'ArrayFieldTest.gif'
    immediate_view             = 'base_view'
    default_view               = 'base_view'
    suppl_views                = ()
    typeDescription            = "ArrayFieldTest"
    typeDescMsgId              = 'description_edit_arrayfieldtest'

    actions =  (


       {'action':      "string:${object_url}/arrayfield_test",
        'category':    "object",
        'id':          'arrayfield_test',
        'name':        'arrayfield_test',
        'permissions': ("View",),
        'condition'  : 'python:1'
       },


    )

    schema = ArrayFieldTest_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    #Methods
    #manually created methods

    def testset(self, value):
        import pdb;pdb.set_trace()
        self.Schema()['names'].fields()[1].set(self,value)
        


registerType(ArrayFieldTest,PROJECTNAME)
# end of class ArrayFieldTest

##code-section module-footer #fill in your manual code here
##/code-section module-footer



