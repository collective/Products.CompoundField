# File: XPointField.py
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

#XPointField




from types import ListType, TupleType, StringTypes
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
from Products.generator import i18n

from Products.CompoundField import config

##code-section module-header #fill in your manual code here
##/code-section module-header

from Products.CompoundField.CompoundField import CompoundField
from XPointWidget import XPointWidget
from XPoint import XPoint


from Products.CompoundField.CompoundField import CompoundField
######CompoundField
schema=Schema((
    IntegerField('x',
        widget=IntegerWidget(
            label='X',
            label_msgid='CompoundField_label_x',
            description_msgid='CompoundField_help_x',
            i18n_domain='CompoundField',
        )
    ),

    IntegerField('y',
        widget=IntegerWidget(
            label='Y',
            label_msgid='CompoundField_label_y',
            description_msgid='CompoundField_help_y',
            i18n_domain='CompoundField',
        )
    ),

),
)




class XPointField(CompoundField):
    ''' '''

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(CompoundField,'__implements__',()),)


    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'xpointfield',
        'widget':XPointWidget,
        'value_class':XPoint,
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })

    security  = ClassSecurityInfo()

    schema=schema

    security.declarePrivate('set')
    security.declarePrivate('get')



registerField(XPointField,
              title='XPointField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



