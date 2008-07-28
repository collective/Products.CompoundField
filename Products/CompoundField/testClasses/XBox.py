# -*- coding: utf-8 -*-
#
# File: XBox.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

from zope.interface import implements
from Products.CompoundField.testClasses.XPoint import XPoint
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin


class XBox:
    """
    """

    ##code-section class-header_XBox #fill in your manual code here
    ##/code-section class-header_XBox


    def __init__(self,p1=None,p2=None,*args,**kwargs):
        self.init_attributes()
        self.p1=p1
        self.p2=p2


    def _init_attributes(self,*args,**kwargs):
        #attributes
        self.p1=None
        self.p1=None
        # automatically set attributes where mutators exist
        for key in kwargs.keys():
            # camel case: variable -> setVariable
            mutatorName = 'set'+key[0].upper()+key[1:]
            mutator = getattr(self, mutatorName)
            if mutator is not None and callable(mutator):
                mutator(kwargs[key])

    def getP1(self):
        return self.p1


    def init_attributes(self):
        #attributes
        self.p1=None
        self.p1=None


    def setP1(self,value):
        self.p1=value


    def __str__(self):
        return "(%s,%s)" %(self.p1,self.p2)
    __repr__=__str__

##code-section module-footer #fill in your manual code here
##/code-section module-footer


