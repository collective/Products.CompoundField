# -*- coding: utf-8 -*-
#
# File: CompoundFieldTestCase.py
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

#
# Base TestCase for CompoundField
#

import os, sys, code
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

from Testing import ZopeTestCase
from Products.PloneTestCase import PloneTestCase
from Products.CompoundField.config import PRODUCT_DEPENDENCIES
from Products.CompoundField.config import DEPENDENCIES

# Add common dependencies
DEPENDENCIES.append('Archetypes')
PRODUCT_DEPENDENCIES.append('MimetypesRegistry')
PRODUCT_DEPENDENCIES.append('PortalTransforms')
PRODUCT_DEPENDENCIES.append('CompoundField')

# Install all (product-) dependencies, install them too
for dependency in PRODUCT_DEPENDENCIES + DEPENDENCIES:
    ZopeTestCase.installProduct(dependency)

ZopeTestCase.installProduct('CompoundField')

PRODUCTS = list()
PRODUCTS += DEPENDENCIES
PRODUCTS.append('CompoundField')

testcase = PloneTestCase.PloneTestCase
##code-section module-before-plone-site-setup #fill in your manual code here
from Globals import package_home
##/code-section module-before-plone-site-setup

PloneTestCase.setupPloneSite(products=PRODUCTS)

class CompoundFieldTestCase(testcase):
    """Base TestCase for CompoundField."""

    ##code-section class-header_CompoundFieldTestCase #fill in your manual code here
    def getInputDir(name,templdir=''):
        samples=os.path.join(package_home(globals()),'input')
        dir=samples
        if templdir:
            dir=os.path.join(dir,templdir)

        return dir
    ##/code-section class-header_CompoundFieldTestCase

    # Commented out for now, it gets blasted at the moment anyway.
    # Place it in the protected section if you need it.
    #def afterSetup(self):
    #    """
    #    """
    #    pass

    def interact(self, locals=None):
        """Provides an interactive shell aka console inside your testcase.

        It looks exact like in a doctestcase and you can copy and paste
        code from the shell into your doctest. The locals in the testcase are
        available, becasue you are in the testcase.

        In your testcase or doctest you can invoke the shell at any point by
        calling::

            >>> self.interact( locals() )

        locals -- passed to InteractiveInterpreter.__init__()
        """
        savestdout = sys.stdout
        sys.stdout = sys.stderr
        sys.stderr.write('='*70)
        console = code.InteractiveConsole(locals)
        console.interact("""
ZopeTestCase Interactive Console
(c) BlueDynamics Alliance, Austria - 2005

Note: You have the same locals available as in your test-case.
""")
        sys.stdout.write('\nend of ZopeTestCase Interactive Console session\n')
        sys.stdout.write('='*70+'\n')
        sys.stdout = savestdout


def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(CompoundFieldTestCase))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


