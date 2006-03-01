# File: XPoint.py
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


class XPoint:
    """
    """

    ##code-section class-header_XPoint #fill in your manual code here
    ##/code-section class-header_XPoint


    def __init__(self,x=0,y=0,*args,**kwargs):
        self.init_attributes()
        self.x=x
        self.y=y


    def _init_attributes(self,*args,**kwargs):
        #attributes
        self.x=None
        self.y=None
        # automatically set attributes where mutators exist
        for key in kwargs.keys():
            # camel case: variable -> setVariable
            mutatorName = 'set'+key[0].upper()+key[1:]
            mutator = getattr(self, mutatorName)
            if mutator is not None and callable(mutator):
                mutator(kwargs[key])

    def init_attributes(self):
        #attributes
        self.x=None 
        self.y=None 
                        

    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
                                                                                                                                                                                                                                                                                                    

    def __str__(self):
        return 'XPoint(%s,%s)' % (self.x,self.y)
                                                                                                                                                                                                                                                                                                    

    def getX(self):
        return self.x
                                                                                                                                                                                                                                                                                                

    def getY(self):
        return self.y
                                                                                                                                                                                                                                                                                                

    def __repr__(self):
        return str(self)
                            

    def setX(self,value):
        self.x=value
                                                                                                                                                                                                                                                                                                

    def setY(self,value):
        self.y=value
                                                                                                                                                                                                                                                                                                

##code-section module-footer #fill in your manual code here
##/code-section module-footer


