# -*- coding: utf-8 -*-
#
# File: testXMLMarshall.py
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

import os, sys
try:
    from Products.PloneTestCase.PloneTestCase import USELAYER
    from Products.PloneTestCase.layer import PloneSite
except:
    USELAYER = False
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) CompoundFieldTest
#

from Testing import ZopeTestCase
from Products.CompoundField.tests.CompoundFieldTestCase import CompoundFieldTestCase

# Import the tested classes
from Products.CompoundField.testClasses.CompoundFieldTest import CompoundFieldTest


class testXMLMarshall(CompoundFieldTestCase):
    """Test-cases for class(es) CompoundFieldTest."""

    ##code-section class-header_testXMLMarshall #fill in your manual code here
    ##/code-section class-header_testXMLMarshall

    def afterSetUp(self):
        """
        """
        pass

    # Manually created methods


def test_suite():
    from unittest import TestSuite
    from Testing.ZopeTestCase.zopedoctest import ZopeDocFileSuite
    from Testing.ZopeTestCase import ZopeDocFileSuite
    ##code-section test-suite-in-between #fill in your manual code here
##/code-section test-suite-in-between


    s = ZopeDocFileSuite('testXMLMarshall.txt',
                         package='Products.CompoundField.doc',
                         test_class=testXMLMarshall)
    if USELAYER:
        s.layer = PloneSite
    return TestSuite((s,
                      ))

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


