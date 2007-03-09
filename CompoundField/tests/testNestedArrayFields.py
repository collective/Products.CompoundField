# -*- coding: utf-8 -*-
#
# File: testNestedArrayFields.py
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

import os, sys
if __name__ == '__main__':
    execfile(os.path.join(sys.path[0], 'framework.py'))

##code-section module-header #fill in your manual code here
##/code-section module-header

#
# Test-cases for class(es) 
#

from Testing import ZopeTestCase
from Products.CompoundField.tests.CompoundFieldTestCase import CompoundFieldTestCase

# Import the tested classes
from Products.CompoundField.testClasses.NestedArrayFieldTest import NestedArrayFieldTest


class testNestedArrayFields(CompoundFieldTestCase):
    """Test-cases for class(es) ."""

    ##code-section class-header_testNestedArrayFields #fill in your manual code here
    ##/code-section class-header_testNestedArrayFields

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
        ZopeDocFileSuite('testNestedArrayFields.txt',
                         package='Products.CompoundField.doc',
                         test_class=testNestedArrayFields),
    ))

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


