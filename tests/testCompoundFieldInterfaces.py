# File: testCompoundFieldInterfaces.py
# 
# Copyright (c) 2005 by eduplone Open Source Business Network EEIG
# Generator: ArchGenXML Version 1.4.0-RC1 devel 
#            http://plone.org/products/archgenxml
#
# This software is released under the German Free Software License (D-FSL).
# The full text of this license is delivered with this product or is available
# at http://www.dipp.nrw.de/d-fsl
#
__author__  = '''Phil Auersperg <phil@bluedynamics.com>, Jens Klein
<jens.klein@jensquadrat.com>'''
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


