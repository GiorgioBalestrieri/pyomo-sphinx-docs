"""
pyomo_sphinx_docs.py
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
    
    for c in model.component_objects(descend_into=False):
        if isinstance(c, pyomo.core.base.Block):
            s += "\n\n"
            s += get_pyomo_model_docs(c, level+1)
        else:
            if c.doc is not None:
                
                # component type and name
                type_name = str(c.type()).split(".")[-1].split("'")[0]
                comp_name = c.name
                if level > 1: comp_name = comp_name.split('.')[-1]
                s += "\n"
                s += f" - ``{type_name}`` ``{c.name}``: "
                
                # component doc
                s += "\n\t"
                s += f"{c.doc}"
                
                # component info
                s += "\n\n\t"
                s += "Properties: " + ", ".join("%s=%s" % (k,v) for k,v in c._pprint()[0] 
                                                if k not in ['Dim', 'Size', 'Active']) 
                s += "\n"
    return s