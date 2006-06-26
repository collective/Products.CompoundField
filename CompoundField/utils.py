# File: utils.py
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

__author__ = """Encolpe Degoute <encolpe.degoute@ingeniweb.com>"""
__docformat__ = 'plaintext'

# utils

def reval(codestring, locals=None, eval=eval):
    """ Restricted execution eval().

        After a suggestion by Tim Peters on comp.lang.python.  locals
        can be given as local namespace to use when evaluating the
        codestring.

        code copied from egenix-mx-base
    """
    if locals is not None:
        return eval(codestring,{'__builtins__':{}},locals)
    else:
        return eval(codestring,{'__builtins__':{}})
