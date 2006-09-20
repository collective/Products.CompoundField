##parameters=fieldname,size

target_field = context.getField(fieldname)

def digIntoArrayField(field, fieldname):
    """
    field is an Arryfield which contains either ArrayField or CompoundField
    the resize call is for one of them.
    The first field is always an int field containing the array size then we can
    ignore it.
    The fieldname is corrupted by the internal ArrayField separator.
    """
    fields = field.getFields()
    if len(fields) < 2:
        return None

    separator = fields[1].separator
    parts = fieldname.split(separator)
    arrayfield_name = parts[1]
    target_fieldname = separator.join(parts[2:])

    compoundfield = field.getField(arrayfield_name)

    for subfield in compoundfield.getFields():
        if subfield.old_name == target_fieldname:
            return subfield
        elif hasattr(subfield, 'separator') and \
             subfield.separator in target_fieldname:
            return digInto(subfield, target_fieldname)

    return None

#
# Dig into fields and sub-schemas to find the good field to resize
#
if not target_field:
    fields = context.Schema().fields()
    for field in fields:
        # if the fieldname contains the field's separator and begins by the
        # field id we dig into its sub-schema
        if hasattr(field, 'separator') and \
           field.separator in fieldname:
            target_field = digIntoArrayField(field, fieldname)

target_field.resize(int(size), context)

return context.REQUEST.RESPONSE.redirect(context.REQUEST['HTTP_REFERER'])
