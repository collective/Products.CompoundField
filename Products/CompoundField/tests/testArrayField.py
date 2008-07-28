# -*- coding: utf-8 -*-
#
# File: testArrayField.py
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
<jens@bluedynamics.com>"""
__docformat__ = 'plaintext'

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) ArrayFieldTest
#

from Testing import ZopeTestCase
from Products.PloneTestCase.PloneTestCase import PloneTestCase

# Import the tested classes
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
    # Manually created methods


def test_suite():
    from unittest import TestSuite
    from Testing.ZopeTestCase.zopedoctest import ZopeDocFileSuite

    ##code-section test-suite-in-between #fill in your manual code here
##/code-section test-suite-in-between


    return TestSuite((
        ZopeDocFileSuite('testArrayField.txt',
                         package='Products.CompoundField.doc',
                         test_class=testArrayField),
    ))

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


