from sets import Set

from Products.CMFCore.utils import getToolByName
from Products.Marshall.handlers.atxml import XmlNamespace
from Products.Marshall.handlers.atxml import SchemaAttribute
from Products.Marshall.handlers.atxml import getRegisteredNamespaces
from Products.CompoundField.ICompoundField import ICompoundField

from Products.Marshall import utils

from Products.Archetypes.debug import log

class CompoundAttribute(SchemaAttribute):
    def processXmlValue(self, context, value):
        """ callback to process text nodes
        """
        # text value is normally irrelevant in compound field
        value = self.parseXmlNode(context, context.node)
        if not value:
            return
        data = context.getDataFor( self.namespace.xmlns )
        data[self.name] = value
        
    def parseXmlNode(self, context, node):
        '''parses the xml node and converts it into a compound field
        compliant dictionary'''

        tagname, namespace = utils.fixtag(node.tag, context.ns_map)
        
        if tagname == 'compound':
            return self.parseCompound(context,node)
        elif tagname == 'array':
            return self.parseArray(context,node)
        elif tagname == 'field':
            return node.text and node.text.strip()

    def parseCompound(self,context,node):
        res={}
        for n in node:
            name = n.attrib.get('name', None)
            if name is None:
               name = n.attrib.get('id', None)
               log("compoundfield %s: 'id' attribute is deprecated, use 'name' instead" % name)
            value = self.parseXmlNode(context, n)
            res[name] = value
        return res
    
    def parseArray(self, context, node):
        res=[]
        for item in node:
            n = item[0]
            value = self.parseXmlNode(context, n)
            res.append(value)
            
        return res
    
    def set(self, instance, data):
        """ set the attribute's value on the instance
        """
        if not data.has_key(self.name):
            return
        
        field = instance.Schema()[self.name]
        value = data[self.name]
        field.getMutator(instance)(value)
        
    
    def serialize(self, dom, parent_node, instance, options ):
        pass

class CompoundFieldNS(XmlNamespace):
    xmlns="http://plone.org/ns/archetypes/compoundfield"
    attributeClass = CompoundAttribute
    attributes = []
    
    
    def getATFields(self):
        return ['array','compound']
    
    def serialize(self, dom, parent_node, instance, options ):
        exclude_attrs = options.get('atns_exclude', () )
        for attribute in self.getAttributes( instance, exclude_attrs):
            attribute.serialize( dom, parent_node, instance, options )

    def deserialize(self, instance, ns_data, options):
        if not ns_data:
            return
            
        for attribute in self.getAttributes( instance ):
            attribute.deserialize( instance, ns_data )

    def processXml(self, context, data_node):

        tagname, namespace = utils.fixtag(data_node.tag, context.ns_map)
        
        if tagname == 'metadata':
            # ignore the container
            return False

        elif tagname in ('compound','array'):
            # basic at field specified, find the matching attribute
            # and annotate the data node with it
            schema_name = data_node.attrib.get('name', None)
            if schema_name is None:
                schema_name = data_node.attrib.get('id',)
                log("field %s: 'id' attribute is deprecated, use 'name' instead" % schema_name)

            assert schema_name, "No field name specified in cf:[array|compound] element"
            #print "field", schema_name
            self.last_schema_id = schema_name
            attribute = self.getAttributeByName(schema_name, context)
            if attribute is None:
                #print "na", schema_name
                return False
            data_node.attribute = attribute
            return True

        return False
    
    def getAttributeByName(self, schema_name, context=None):
        if context is not None: # and schema_name not in self.at_fields:
            if not context.instance.Schema().has_key( schema_name ):
                return
                raise AssertionError, \
                      "invalid attribute %s" % (schema_name)
        
        attribute = self.attributeClass( schema_name )
        attribute.setNamespace( self )
        
        return attribute
    
    def getAttributes(self, instance, exclude_attrs=()):

        # remove fields delegated to other namespaces

        fields = instance.Schema().fields()
        for f in fields:
            if ICompoundField.isImplementedBy(f):
                yield self.getAttributeByName(f.getName())


