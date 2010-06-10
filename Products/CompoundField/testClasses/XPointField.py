# -*- coding: utf-8 -*-
#
# File: XPointField.py
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

from Products.CompoundField import config

##code-section module-header #fill in your manual code here
##/code-section module-header

from zope.interface import implements
from Products.CompoundField.CompoundField import CompoundField
from Products.CompoundField.testClasses.XPointWidget import XPointWidget
from Products.CompoundField.testClasses.XPoint import XPoint
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin



from Products.CompoundField.CompoundField import CompoundField
######CompoundField
schema = Schema((

    IntegerField(
        name='x',
        widget=IntegerField._properties['widget'](
            label='X',
            label_msgid='CompoundField_label_x',
            i18n_domain='CompoundField',
        ),
    ),
    IntegerField(
        name='y',
        widget=IntegerField._properties['widget'](
            label='Y',
            label_msgid='CompoundField_label_y',
            i18n_domain='CompoundField',
        ),
    ),

),
)




class XPointField(CompoundField):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header



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



