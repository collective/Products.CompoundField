# File: XBox.py
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


##code-section module-header #fill in your manual code here
##/code-section module-header


from XPoint import XPoint

class XBox:
    ''' '''
    __implements__ = ()

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



