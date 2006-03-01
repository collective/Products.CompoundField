# File: XPointField.py
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

#XPointField

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
try:
    from Products.generator import i18n
except ImportError:
    from Products.Archetypes.generator import i18n

from Products.CompoundField import config

##code-section module-header #fill in your manual code here
##/code-section module-header

from Products.CompoundField.CompoundField import CompoundField
from Products.CompoundField.testClasses.XPointWidget import XPointWidget
from Products.CompoundField.testClasses.XPoint import XPoint


from Products.CompoundField.CompoundField import CompoundField
######CompoundField
schema = Schema((

    IntegerField(
        name='x',
        widget=IntegerWidget(
            label='X',
            label_msgid='CompoundField_label_x',
            i18n_domain='CompoundField',
        )
    ),

    IntegerField(
        name='y',
        widget=IntegerWidget(
            label='Y',
            label_msgid='CompoundField_label_y',
            i18n_domain='CompoundField',
        )
    ),

),
)



class XPointField(CompoundField):
    """
    """
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



