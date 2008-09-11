# -*- coding: utf-8 -*-
#
# File: CompoundField.py
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


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "CompoundField"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
ADD_CONTENT_PERMISSIONS = {
    'CompoundFieldTest': 'CompoundField: Add CompoundFieldTest',
    'ArrayFieldTest': 'CompoundField: Add ArrayFieldTest',
    'NestedArrayFieldTest': 'CompoundField: Add NestedArrayFieldTest',
}

setDefaultRoles('CompoundField: Add CompoundFieldTest', ('Manager','Owner'))
setDefaultRoles('CompoundField: Add ArrayFieldTest', ('Manager','Owner'))
setDefaultRoles('CompoundField: Add NestedArrayFieldTest', ('Manager','Owner'))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
COMPOUND_FIELD_SEPERATOR='|'
ARRAY_FIELDNAME_SEPARATOR = ':'
HAS_MARSHALLER=False
EVIL_EVAL=False
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from Products.CompoundField.AppConfig import *
except ImportError:
    pass
