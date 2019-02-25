"""
main.py
====================

Utilities to automatically generate Sphinx documentation
for Pyomo models.
"""

import pyomo

def get_pyomo_model_docs(model, level=0, header_subs=['-', '~', '+']):
    """Create ``.rst`` documentation from Pyomo model.
    
    Recursively calls itself if the model has nested components.
    """
    
    name = model.name
    if name == 'unknown': name = 'model'
    
    s = f"{name} - documentation \n"
    s += header_subs[level] * (len(s) - 1) # add line to create header
    s += "\n"
    
    for component in model.component_objects(descend_into=False):
        if isinstance(component, pyomo.core.base.Block):
            s += "\n\n"
            s += get_pyomo_model_docs(component, level+1)
        else:
            if component.doc is not None:
                s += "\n"
                s += get_component_docs(component, level)
                s += "\n"
    return s


def get_component_docs(component, level):
    """
    Get .rst docstring for a Pyomo Component.
    """
    skip_props = ['Dim', 'Size', 'Active']

    # component type and name
    type_name = str(component.type()).split(".")[-1].split("'")[0]
    comp_name = component.name
    if level > 1: comp_name = comp_name.split('.')[-1]

    comp_str = ""
    comp_str += f" - ``{type_name}`` ``{component.name}``: "
    
    # component doc
    comp_str += "\n\t"
    comp_str += f"{component.doc}"
    
    # component info
    comp_str += "\n\n\t"
    comp_str += "Properties: " + get_component_properties_docs(component, skip_props)

    return comp_str


def get_component_properties_docs(component, skip_props=[]):
    """
    Get .rst docs for Pyomo Component properties. 
    """
    return ", ".join("%s=%s" % (k,v) for k,v in component._pprint()[0] 
                     if k not in skip_props) 
