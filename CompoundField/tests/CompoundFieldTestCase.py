# File: CompoundFieldTestCase.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Base TestCase for CompoundField
#
from Testing import ZopeTestCase
from Products.PloneTestCase import PloneTestCase

ZopeTestCase.installProduct('Archetypes')
ZopeTestCase.installProduct('PortalTransforms', quiet=1)
ZopeTestCase.installProduct('MimetypesRegistry', quiet=1)
ZopeTestCase.installProduct('CompoundField')
# If the products's config includes DEPENDENCIES, install them too
try:
    from Products.CompoundField.config import DEPENDENCIES
except:
    DEPENDENCIES = []
for dependency in DEPENDENCIES:
    ZopeTestCase.installProduct(dependency)

PRODUCTS = ('Archetypes', 'CompoundField')

testcase = PloneTestCase.PloneTestCase
PloneTestCase.setupPloneSite(products=PRODUCTS)

class CompoundFieldTestCase(testcase):
    """ Base TestCase for CompoundField"""
    ##code-section class-header_CompoundFieldTestCase #fill in your manual code here
    ##/code-section class-header_CompoundFieldTestCase

    # Commented out for now, it gets blasted at the moment anyway.
    # Place it in the protected section if you need it.
    #def afterSetUp(self):
    #    """
    #    """
    #    pass

##code-section module-footer #fill in your manual code here
##/code-section module-footer



