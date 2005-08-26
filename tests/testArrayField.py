# File: testArrayField.py
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
# test-cases for class(es) ArrayFieldTest
#
import os, sys
from Testing import ZopeTestCase
from Products.PloneTestCase.PloneTestCase import PloneTestCase
# import the tested classes
from Products.CompoundField.testClasses.ArrayFieldTest import ArrayFieldTest
from Products.CompoundField.ArrayField import ArrayField

class testArrayField(PloneTestCase):
    """ test-cases for class(es) 
    """

    ##code-section class-header_testArrayField #fill in your manual code here
    ##/code-section class-header_testArrayField

    def afterSetUp(self):
        """
        """
        pass


    # from class ArrayFieldTest:
    def test_arrayfield_test(self):
        """ 
        """
        #Uncomment one of the following lines as needed
        ##self.loginAsPortalOwner()
        ##o=ArrayFieldTest('temp_ArrayFieldTest')
        ##self.folder._setObject('temp_ArrayFieldTest', o)
        pass
        


    # Manually created methods


def test_suite():
    from unittest import TestSuite
    from Testing.ZopeTestCase.zopedoctest import ZopeDocFileSuite

    return TestSuite((
        ZopeDocFileSuite('testArrayField.txt',
                         package='Products.CompoundField.doc',
                         test_class=testArrayField),
    ))


if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-footer #fill in your manual code here
##/code-section module-footer



