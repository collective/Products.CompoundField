# File: XBox.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

from Products.CompoundField.testClasses.XPoint import XPoint
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


