## Script (Python) "at_download"
##title=Download a file keeping the original uploaded filename
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath

#XXX:evil hack for at_download, since the normal way doesnt find the field 
from Products.CompoundField.utils import getNestedField
if traverse_subpath:
    field = getNestedField(context,traverse_subpath[0])
else:
    field = context.getPrimaryField()
    
#raise 'Test',field
return field.download(context)
