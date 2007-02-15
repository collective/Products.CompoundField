# -*- coding: utf-8 -*-
#
# File: CompoundField.py
#
# Copyright (c) 2007 by eduplone Open Source Business Network EEIG (2005-2006),
# BlueDynamics Alliance
# Generator: ArchGenXML Version 1.5.2
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


# There are three ways to inject custom code here:
#
#   - To set global configuration variables, create a file AppConfig.py.
#       This will be imported in config.py, which in turn is imported in
#       each generated class and in this file.
#   - To perform custom initialisation after types have been registered,
#       use the protected code section at the bottom of initialize().
#   - To register a customisation policy, create a file CustomizationPolicy.py
#       with a method register(context) to register the policy.

import logging
logger = logging.getLogger('CompoundField')
logger.info('Installing Product')

try:
    import CustomizationPolicy
except ImportError:
    CustomizationPolicy = None

import os, os.path
from Globals import package_home
from Products.CMFCore import utils as cmfutils

try: # New CMF
    from Products.CMFCore import permissions as CMFCorePermissions 
except: # Old CMF
    from Products.CMFCore import CMFCorePermissions

from Products.CMFCore import DirectoryView
from Products.CMFPlone.utils import ToolInit
from Products.Archetypes.atapi import *
from Products.Archetypes import listTypes
from Products.Archetypes.utils import capitalize
from config import *

DirectoryView.registerDirectory('skins', product_globals)
DirectoryView.registerDirectory('skins/CompoundField',
                                    product_globals)

##code-section custom-init-head #fill in your manual code here
try:
    from Products.Marshall.handlers.atxml import registerNamespace
    from Products.CompoundField.cfns import CompoundFieldNS
    registerNamespace( CompoundFieldNS )
    HAS_MARSHALLER=True

except ImportError:
    HAS_MARSHALLER=False



##/code-section custom-init-head


def initialize(context):
    ##code-section custom-init-top #fill in your manual code here
    from AccessControl import allow_module
    allow_module('Products.CompoundField.utils')
    ##/code-section custom-init-top

    # imports packages and types for registration
    import testClasses

    import CompoundField
    import CompoundWidget
    import ArrayField
    import ArrayWidget
    import EnhancedArrayWidget
    import ICompoundField
    import IArrayField

    # Initialize portal content
    content_types, constructors, ftis = process_types(
        listTypes(PROJECTNAME),
        PROJECTNAME)

    cmfutils.ContentInit(
        PROJECTNAME + ' Content',
        content_types      = content_types,
        permission         = DEFAULT_ADD_CONTENT_PERMISSION,
        extra_constructors = constructors,
        fti                = ftis,
        ).initialize(context)

    # Apply customization-policy, if theres any
    if CustomizationPolicy and hasattr(CustomizationPolicy, 'register'):
        CustomizationPolicy.register(context)
        print 'Customization policy for CompoundField installed'

    ##code-section custom-init-bottom #fill in your manual code here
    ##/code-section custom-init-bottom

