# -*- coding: utf-8 -*-
#
# File: EnhancedArrayWidget.py
#
# Copyright (c) 2008 by BlueDynamics Alliance (since 2007), 2005-2006 by
# eduplone Open Source Business Network EEIG
# Generator: ArchGenXML Version 2.2 (svn)
#            http://plone.org/products/archgenxml
#
# German Free Software License (D-FSL)
#

__author__ = """Sune Broendum Woeller <sune@woeller.dk>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Acquisition import aq_base

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.Registry import registerWidget
from Products.Archetypes.utils import DisplayList
from Products.Archetypes import config as atconfig
from Products.Archetypes.Widget import *
from Products.Archetypes.Widget import TypesWidget

from Products.CompoundField import config

##code-section module-header #fill in your manual code here
#from Products.Archetypes.ArchetypeTool import _guessPackage
from Products.Archetypes.ArchetypeTool import WidgetWrapper
from Products.CompoundField import config
from Products.CompoundField.utils import *
import re
##/code-section module-header

from zope.interface import implements
from Products.CompoundField.ArrayWidget import ArrayWidget
from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin



class EnhancedArrayWidget(ArrayWidget):
    """
    """
    ##code-section class-header #fill in your manual code here
    ##/code-section class-header


    _properties = ArrayWidget._properties.copy()
    _properties.update({
        'macro' : 'EnhancedArrayWidget',
        ##code-section widget-properties #fill in your manual code here
        ##/code-section widget-properties

        })

    security = ClassSecurityInfo()


    def process_form(self, instance, field, form, empty_marker=None,
                     emptyReturnsMarker=False):
        #print 'processss_form:',form
        value={}
        #resize the schema if we are supplied with a new size:
        sizeFieldName = field.Schema().fields()[0].getName()
        if form.has_key(sizeFieldName):
            field.resize(int(form[sizeFieldName]), instance)
        # we need to get the fields again after a resize
        for f in field.Schema().fields()[1:]:
            fname=getattr(f,'old_name',field.getName())
            value[fname]=f.widget.process_form(instance,f,form,empty_marker)

        return value, {}

    def getTypes(self, context, typepath=None):
        """
        Get the types for the content type
        """
        atool = getToolByName(context, 'archetype_tool')
        atool = getattr(atool, "tool", atool) # Plone 4 compatibility
        portal_type = context.portal_type

        # Initialize the recursion
        if typepath == None: typepath = context.__module__.split(".")

        # Try the whole recursion again without preceding 'Products.' part
        if typepath == ["Products"]: typepath = context.__module__.split(".")[1:]

        # End recursion
        if not typepath: raise KeyError, context.__module__

        try:
            # Try to find the current portal type's module in all the registered types
            return atool.listTypes(".".join(typepath), portal_type)
        except KeyError, ex:
            # Strip off the last part of the path and try again until the path is empty
            return self.getTypes(context, typepath[:-1])

    def getSubFieldWidgetHtml(self, context, field_name):
        """
        Get the widget html for a subfield of an ArrayField.
        """
        # The following code is adapted from getWidgets in ArchetypeTool
        t = self.getTypes(context, context.__module__.split("."))[0]
        instance = t('fake_instance')
        instance._at_is_fake_instance = True
        # XXX _is_fake_instance will go away in AT 1.4
        instance._is_fake_instance = True
        wrapped = instance.__of__(context)
        wrapped.initializeArchetype()

        # Get the field of the new instance. The field may be nested
        # in other fields schema. We use getNestedField to
        # get the nested field.
        field = getNestedField(wrapped, field_name)
        # We require the widget to contain a least one element when created, to
        # have something to render.
        # (Remember that size is element 0)
        if len(field.getFields()) >1:
            firstSubField = field.getFields()[1]
            widget = firstSubField.widget
            subfield_name = firstSubField.getName()
            accessor = firstSubField.getAccessor(wrapped)
        else:
            firstSubField=None
            widget=None
            subfield_name=''
            accessor=None

        wrapped_widget = (WidgetWrapper(
            field_name=subfield_name,
            mode='edit',
            widget=widget,
            instance=wrapped,
            field=firstSubField,
            accessor=accessor))

        #render the widget with the help of a simple page template
        html = context.renderArrayWidgetHtml(widget = wrapped_widget, field = firstSubField, mode = 'edit')

        #process the html of the rendered widget to be able to include it in a javascript

        #strip whitespace of every line
        lines=[]
        for l in html.splitlines():
            l2=l.strip()
            if l2:
                lines.append(l2)
        html = " ".join(lines)

        # Javascript escapes
        html = html.replace('\\','\\\\')
        html = html.replace("'","\\'")
        html = html.replace('"','\\"')
        html = html.replace('\n','\\n')
        html = html.replace('\t','\\t')

        # hide the script-tags from the browser
        html = html.replace('<script>', "<scr' + \n 'ipt>")
        html = html.replace('</script>', "</scr' + \n 'ipt>")

        seperator = config.COMPOUND_FIELD_SEPERATOR
        #from Products.zdb import set_trace; set_trace()

        # Replace the index (000) of the subfield_name in any html attribute with
        # a marker, we easier can replace with the new index in the javascript code.


# problem with regex when trying to alter zero indexes (000) with index marker
# when using compound fields inside enhanced array widget. altered the regex
# with string.replace() call.



##        (fname, index) = self.splitArrayFieldName(subfield_name)
##        if seperator == '|':
##            fname = fname.replace('|', '\|')
##
##        FIELD_NAME_INDEX_REGEX = re.compile(
##            r'=\\"' +  # beginning of attribute
##            r'([^"]*-)*' + # optional 'archetype-field-name-'
##            r'(' + fname + r':)(' + index + ')' + # the prefixed field name and index
##            r'(\|[^"]+)*' + # optional sub field names
##            r'(_[^"]*)*\\"' # optional text after the field name
##            )
##
##        def match_handler(mo):
##            g = mo.group
##            return '="' + (g(1) or '') + (g(2) or '') + '__WIDGET_INDEX_MARKER__' + (g(4) or '') + (g(5) or '') + '"'

        #html = FIELD_NAME_INDEX_REGEX.sub(match_handler, html, 0)

        html = html.replace('%s000' % config.ARRAY_FIELDNAME_SEPARATOR,
                            '%s__WIDGET_INDEX_MARKER__' % config.ARRAY_FIELDNAME_SEPARATOR)

        return html

    def splitArrayFieldName(self, field_name):
        # Split an array field name in name part and index part.
        # We split at the last ARRAY_FIELDNAME_SEPARATOR.
        split_point = field_name.rfind(config.ARRAY_FIELDNAME_SEPARATOR)
        fname = field_name[0:split_point]
        index = field_name[split_point+1:]
        return (fname, index)


registerWidget(EnhancedArrayWidget,
               title='EnhancedArrayWidget',
               description=('no description given'),
               used_for=('Products.Archetypes.Field.StringField',)
               )
##code-section module-footer #fill in your manual code here
##/code-section module-footer



