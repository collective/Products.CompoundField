""" Extensions/Install.py """

# Copyright (c) 2005 by eduplone Open Source Business Network EEIG
#
# Generated: 
# Generator: ArchGenXML Version 1.4.0-RC1 devel
#            http://plone.org/products/archgenxml
#
# This software is released under the German Free Software License (D-FSL).
# The full text of this license is delivered with this product or is available
# at http://www.dipp.nrw.de/d-fsl
#
__author__    = '''Phil Auersperg <phil@bluedynamics.com>, Jens Klein
<jens.klein@jensquadrat.com>'''
__docformat__ = 'plaintext'
__version__   = '$ Revision 0.0 $'[11:-2]

import os.path
import sys
from StringIO import StringIO

from App.Common import package_home
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.utils import manage_addTool
from Products.ExternalMethod.ExternalMethod import ExternalMethod
from zExceptions import NotFound, BadRequest

from Products.Archetypes.Extensions.utils import installTypes
from Products.Archetypes.Extensions.utils import install_subskin
try:
    from Products.Archetypes.lib.register import listTypes
except ImportError:
    from Products.Archetypes.public import listTypes
from Products.CompoundField.config import PROJECTNAME
from Products.CompoundField.config import product_globals as GLOBALS

def install(self):
    """ External Method to install CompoundField """
    out = StringIO()
    print >> out, "Installation log of %s:" % PROJECTNAME

    # If the config contains a list of dependencies, try to install
    # them.  Add a list called DEPENDENCIES to your custom
    # AppConfig.py (imported by config.py) to use it.
    try:
        from Products.CompoundField.config import DEPENDENCIES
    except:
        DEPENDENCIES = []
    portal = getToolByName(self,'portal_url').getPortalObject()
    quickinstaller = portal.portal_quickinstaller
    for dependency in DEPENDENCIES:
        print >> out, "Installing dependency %s:" % dependency
        quickinstaller.installProduct(dependency)
        get_transaction().commit(1)

    classes = listTypes(PROJECTNAME)
    installTypes(self, out,
                 classes,
                 PROJECTNAME)
    install_subskin(self, out, GLOBALS)


    # try to call a workflow install method
    # in 'InstallWorkflows.py' method 'installWorkflows'
    try:
        installWorkflows = ExternalMethod('temp','temp',PROJECTNAME+'.InstallWorkflows', 'installWorkflows').__of__(self)
    except NotFound:
        installWorkflows = None

    if installWorkflows:
        print >>out,'Workflow Install:'
        res = installWorkflows(self,out)
        print >>out,res or 'no output'
    else:
        print >>out,'no workflow install'


    # enable portal_factory for given types
    factory_tool = getToolByName(self,'portal_factory')
    factory_types=[
        ] + factory_tool.getFactoryTypes().keys()
    factory_tool.manage_setPortalFactoryTypes(listOfTypeIds=factory_types)

    # For plone 2.1, allow the easy registering of stylesheets
    from Products.CompoundField.config import HAS_PLONE21
    if HAS_PLONE21:
        try:
            from Products.CompoundField.config import STYLESHEETS
        except:
            STYLESHEETS = []
        try:
            from Products.CompoundField.config import JAVASCRIPTS
        except:
            JAVASCRIPTS = []
        portal_css = getToolByName(portal, 'portal_css')
        portal_javascripts = getToolByName(portal, 'portal_javascripts')
        for stylesheet in STYLESHEETS:
            try:
                portal_css.unregisterResource(stylesheet['id'])
            except:
                pass
            defaulttitle = '%s %s' % (PROJECTNAME, stylesheet['id'])
            defaults = {'id': '',
            'expression': None,
            'media': 'all',
            'title': defaulttitle,
            'enabled': True}
            defaults.update(stylesheet)
            portal_css.manage_addStylesheet(**defaults)
        for javascript in JAVASCRIPTS:
            try:
                portal_javascripts.unregisterResource(stylesheet['id'])
            except:
                pass
            defaults = {'id': '',
            'expression': '', 
            'inline': False,
            'enabled': True,
            'cookable': True}
            defaults.update(javascript)
            portal_javascripts.registerScript(**defaults)

    # try to call a custom install method
    # in 'AppInstall.py' method 'install'
    try:
        install = ExternalMethod('temp','temp',PROJECTNAME+'.AppInstall', 'install')
    except NotFound:
        install = None

    if install:
        print >>out,'Custom Install:'
        res = install(self)
        if res:
            print >>out,res
        else:
            print >>out,'no output'
    else:
        print >>out,'no custom install'
    return out.getvalue()

def uninstall(self):
    out = StringIO()

    # try to call a workflow uninstall method
    # in 'InstallWorkflows.py' method 'uninstallWorkflows'
    try:
        installWorkflows = ExternalMethod('temp','temp',PROJECTNAME+'.InstallWorkflows', 'uninstallWorkflows').__of__(self)
    except NotFound:
        installWorkflows = None

    if installWorkflows:
        print >>out,'Workflow Uninstall:'
        res = uninstallWorkflows(self,out)
        print >>out,res or 'no output'
    else:
        print >>out,'no workflow uninstall'

    # try to call a custom uninstall method
    # in 'AppInstall.py' method 'uninstall'
    try:
        uninstall = ExternalMethod('temp','temp',PROJECTNAME+'.AppInstall', 'uninstall')
    except:
        uninstall = None

    if uninstall:
        print >>out,'Custom Uninstall:'
        res = uninstall(self)
        if res:
            print >>out,res
        else:
            print >>out,'no output'
    else:
        print >>out,'no custom uninstall'

    return out.getvalue()
