"""
"""
from Products.CompoundField.config import *
from Acquisition import ExplicitAcquisitionWrapper

def getCompoundFieldSeperator():
    """ For access to COMPOUND_FIELD_SEPERATOR in the skin.
    """
    return COMPOUND_FIELD_SEPERATOR


def getNestedField(context, field_name):
    """ 
    """
    schema = context.Schema().copy()
    # top-level field:
    simple_field_names = field_name.split(COMPOUND_FIELD_SEPERATOR)
    toplevel_field_name = simple_field_names[0]
    toplevel_field = schema.get(toplevel_field_name)
    
    prefix = toplevel_field_name
    field = toplevel_field
    for f_name in simple_field_names[1:]:
        f_schema = field.Schema()
        full_name = prefix + COMPOUND_FIELD_SEPERATOR + f_name
        field = f_schema.get( full_name )
        prefix = full_name
    return ExplicitAcquisitionWrapper(field, context)
