# -*- coding: utf-8 -*-
#
# File: testCompoundFieldInterfaces.py
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
# Interface tests
#

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

from Interface import Implements

from Products.CompoundField.tests.CompoundFieldTestCase import CompoundFieldTestCase


from Interface.Verify import verifyClass


from Products.CompoundField.CompoundField import CompoundField

from Products.CompoundField.ICompoundField import ICompoundField




class testCompoundFieldInterfaces(CompoundFieldTestCase):
        
    def testInterfacesForCompoundField(self):
        '''test interface compliance for class CompoundField'''

        
    
        self.failUnless(verifyClass(ICompoundField, CompoundField))
    
        
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testCompoundFieldInterfaces))
    return suite

if __name__ == '__main__':
    framework()


