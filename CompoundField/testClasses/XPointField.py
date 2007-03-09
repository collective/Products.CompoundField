# -*- coding: utf-8 -*-
#
# File: XPointField.py
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
<jens.klein@jensquadrat.com>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base
from Products.CMFCore.utils import getToolByName
from Products.Archetypes.Field import ObjectField, encode, decode
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
from Products.CompoundField.CompoundField import CompoundField
from Products.CompoundField.testClasses.XPointWidget import XPointWidget
from Products.CompoundField.testClasses.XPoint import XPoint


from Products.CompoundField.CompoundField import CompoundField
schema = Schema((

    IntegerField(
        name='x',
        widget=IntegerField._properties['widget'](
            label='X',
            label_msgid='CompoundField_label_x',
            i18n_domain='CompoundField',
        )
    ),

    IntegerField(
        name='y',
        widget=IntegerField._properties['widget'](
            label='Y',
            label_msgid='CompoundField_label_y',
            i18n_domain='CompoundField',
        )
    ),

),
)


##code-section module-header #fill in your manual code here
##/code-section module-header


class XPointField(CompoundField):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(CompoundField,'__implements__',()),)


    _properties = CompoundField._properties.copy()
    _properties.update({
        'type': 'xpointfield',
        'widget': XPointWidget,
        'value_class': XPoint,
        ##code-section field-properties #fill in your manual code here
        ##/code-section field-properties

        })
        
    schema = schema
    security  = ClassSecurityInfo()
    ##code-section security-declarations #fill in your manual code here
    ##/code-section security-declarations

    security.declarePrivate('get')
    security.declarePrivate('getRaw')
    security.declarePrivate('set')


registerField(XPointField,
              title='XPointField',
              description='')

##code-section module-footer #fill in your manual code here
##/code-section module-footer



