# -*- coding: utf-8 -*-
#
# File: XPointWidget.py
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



class XPointWidget(TypesWidget):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(TypesWidget,'__implements__',()),)

    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : 'XPointWidget',
        'size' : '30',
        'maxlength' : '255',
        ##code-section widget-properties #fill in your manual code here
        ##/code-section widget-properties

        })

    security = ClassSecurityInfo()



registerWidget(XPointWidget,
               title='XPointWidget',
               description=('no description given'),
               used_for=('Products.Archetypes.Field.StringField',)
               )
##code-section module-footer #fill in your manual code here
##/code-section module-footer



