# -*- coding: utf-8 -*-
#
# File: testCompoundField.py
#
# Copyright (c) 2006 by eduplone Open Source Business Network EEIG
# Generator: ArchGenXML Version 1.5.0 svn/devel
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
# Test-cases for class(es) CompoundFieldTest
#

from Testing import ZopeTestCase
from Products.CompoundField.config import *
from Products.CompoundField.tests.CompoundFieldTestCase import CompoundFieldTestCase

# Import the tested classes
from Products.CompoundField.testClasses.CompoundFieldTest import CompoundFieldTest
from Products.CompoundField.CompoundWidget import CompoundWidget
from Products.CompoundField.CompoundField import CompoundField
from Products.CompoundField.testClasses.XPoint import XPoint

##code-section module-beforeclass #fill in your manual code here
##/code-section module-beforeclass


class testCompoundField(CompoundFieldTestCase):
    """ test-cases for class(es) CompoundFieldTest
    """

    ##code-section class-header_testCompoundField #fill in your manual code here

    #this can be passed to field.set()

    pointdict_set={'x':(1,),'y':(2,)}

    boxdict_set= {
              'p1':
                (
                  { 'x':
                     ('1',),
                    'y':
                     (2,)
                  },

                ),
              'p2':
                (
                  { 'x':
                     (3,),
                    'y':
                     (4,)
                  },

                )
            }

    #what comes out from widget.process_form
    boxdict_process_form= {
              'p1':
                (
                  { 'x':
                     ('1',{}),
                    'y':
                     ('2',{})
                  },{}

                ),
              'p2':
                (
                  { 'x':
                     ('3',{}),
                    'y':
                     ('4',{})
                  },{}

                )
            }

    pointdict_process_form={'x':('1',{}),'y':('2',{})}

    #this gets returned by field.getRaw(
    boxdict_getraw= {
              'p1':
                (
                  { 'x':
                     (1,{}),
                    'y':
                     (2,{})
                  },{}

                ),
              'p2':
                (
                  { 'x':
                     (3,{}),
                    'y':
                     (4,{})
                  },{}

                )
            }

    pointdict_getraw={'x':(1,{}),'y':(2,{})}

    #these come from field.get()
    pointdict_get={'x':1,'y':2}

    boxdict_get= {
              'p1':
                {'x':1,
                 'y':2
                },
              'p2':
                { 'x':3,
                  'y':4
                  }
              }

    ##/code-section class-header_testCompoundField

    def afterSetUp(self):
        self.loginAsPortalOwner()
        pt=self.portal.portal_types
        pt.constructContent('CompoundFieldTest',self.folder,'cft')
        pt.constructContent('CompoundFieldTest',self.folder,'cft1')

    def test_nestedCompoundField(self):
        """
        """

        o=self.folder.cft
        o.update(box=self.boxdict_set)
        r=o.getBox()

        self.assertEqual(XPoint(1,2),r.p1)
        self.assertEqual(XPoint(3,4),r.p2)

    def test_simpleCompoundField(self):
        """
        """

        o=self.folder.cft
        o.update(point=self.pointdict_set,point2=self.pointdict_set)
        r=o.getPoint()
        self.assertEqual(1,r['x'])
        self.assertEqual(2,r['y'])
        self.assertEqual(r,self.pointdict_get)

        p2=o.getPoint2()
        self.assertEqual(p2,XPoint(1,2))

        #test the field accessor
        p=o.Schema()['point']
        px=o.Schema()['point'].Schema()['x']
        assert p.getAccessor(o),'field p has no accessor'
        assert px.getAccessor(o),'field px has no accessor'
        self.assertEqual(px.getAccessor(o)(),1)
        self.assertEqual(px.getEditAccessor(o)(),1)

        o.update(point2=XPoint(-1,0))
        self.assertEqual(o.getPoint2(),XPoint(-1,0))

    def test_simpleCompoundWidget(self):
        """
        """
        instance=self.folder.cft
        field=instance.Schema()['point']
        #print field.widget.getName()

        form={
            'point|x':'1',
            'point|y':'2',
            }

        result = field.widget.process_form(instance, field, form,
                                         empty_marker=[])
        self.assertEqual(result[0],self.pointdict_process_form)

        self.assertEqual(instance.Schema()['point2'].value_class,XPoint)

    def test_nestedCompoundWidget(self):
        """
        """
        instance=self.folder.cft
        field=instance.Schema()['box']
        #print field.widget.getName()

        form={
            'box|p1|x':'1',
            'box|p1|y':'2',
            'box|p2|x':'3',
            'box|p2|y':'4',
            }

        result = field.widget.process_form(instance, field, form,
                                         empty_marker=[])

        self.assertEqual(result[0],self.boxdict_process_form)

    # Manually created methods

    def test_nestedCompoundFieldFull(self):
        instance=self.folder.cft1

        form={
            'box|p1|x':'1',
            'box|p1|y':'2',
            'box|p2|x':'3',
            'box|p2|y':'4',
            'point|x':'1',
            'point|y':'2',
            'point2|x':'1',
            'point2|y':'2',

            }

        result = instance.processForm(values=form)
        #print instance.getBox()
        #print instance.getPoint()
        self.assertEqual(instance.getPoint(),self.pointdict_get)
        self.assertEqual(instance.getPoint2(),XPoint(1,2))
        self.assertEqual(instance.getRawBox(),self.boxdict_get)
    # Manually created methods

def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(testCompoundField))
    return suite

##code-section module-footer #fill in your manual code here
##/code-section module-footer

if __name__ == '__main__':
    framework()


