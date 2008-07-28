# -*- coding: utf-8 -*-
#
# File: ArrayWidget.py
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
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Registry import registerWidget
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.Archetypes.Widget import TypesWidget

from Products.CompoundField import config

##code-section module-header #fill in your manual code here
##/code-section module-header

from zope.interface import implements
from Products.CompoundField.CompoundWidget import CompoundWidget
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class ArrayWidget(CompoundWidget):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    _properties = CompoundWidget._properties.copy()
    _properties.update({
        'macro' : 'ArrayWidget',
        ##code-section widget-properties #fill in your manual code here
        ##/code-section widget-properties

        })

    security = ClassSecurityInfo()



registerWidget(ArrayWidget,
               title='ArrayWidget',
               description=('no description given'),
               used_for=('Products.Archetypes.Field.StringField',)
               )
##code-section module-footer #fill in your manual code here
##/code-section module-footer



