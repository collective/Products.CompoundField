# File: CompoundWidget.py
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
from Products.Archetypes.Widget import TypesWidget

from types import ListType, TupleType, StringTypes
from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Field import ObjectField,encode,decode
from Products.Archetypes.Registry import registerField
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.generator import i18n

from Products.CompoundField import config

##code-section module-header #fill in your manual code here
from Products.CompoundField.ICompoundField import ICompoundField
##/code-section module-header



class CompoundWidget(TypesWidget):
    ''' '''

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    __implements__ = (getattr(TypesWidget,'__implements__',()),)

    _properties = TypesWidget._properties.copy()
    _properties.update({
        'macro' : 'CompoundWidget',
        'size' : '30',
        'maxlength' : '255',
        ##code-section widget-properties #fill in your manual code here
        ##/code-section widget-properties

        })

    security = ClassSecurityInfo()


    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False):
            
        value={}
        for f in field.Schema().fields():
            fname=getattr(f,'old_name',field.getName())
            value[fname]=f.widget.process_form(instance,f,form,empty_marker)
            
        return value, {}



##code-section module-footer #fill in your manual code here
##/code-section module-footer







