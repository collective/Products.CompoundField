# -*- coding: utf-8 -*-
#
# File: testCompoundFieldInterfaces.py
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


