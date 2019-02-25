"""
diet.py
=======

This module contains an example of a model for the diet problem.
"""

from pyomo import environ as pe
from pyomo.environ import (AbstractModel, Set, Param, 
    Var, Expression, Objective, Constraint, 
    inequality, summation)

infinity = float('inf')


def create_model():
    """Create a :class:`pyomo.environ.AbstracModel` 
    for the diet problem"""
    
    m = AbstractModel("diet")

    #--------------------------
    #         Sets
    #--------------------------

    m.F = Set(doc="Foods. :math:`\\mathcal{F}`")
    m.N = Set(doc="Nutrients. :math:`\\mathcal{N}`")

    #--------------------------
    #       Parameters
    #--------------------------

    m.cost = Param(m.F, 
        within = pe.NonNegativeReals, 
        doc = """Cost of each food. 
        :math:`c_f \\geq 0`""")

    m.content = Param(m.F, m.N, 
        within = pe.NonNegativeReals, 
        doc = """Amount of nutrient in each food. 
        :math:`a_{f,n} \\geq 0`""")

    m.min_intake = Param(m.N, 
        within = pe.NonNegativeReals, 
        default = 0.0, 
        doc = """Lower bound on each nutrient. 
        :math:`y^{min}_n`""")

    m.max_intake = Param(m.N, 
        within = pe.NonNegativeReals, 
        default = infinity, 
        doc= """Upper bound on each nutrient. 
        :math:`y^{max}_n`""")

    m.volume = Param(m.F, 
        within = pe.PositiveReals, 
        doc = """Volume per serving of food. 
        :math:`v_f`""")

    m.max_volume = Param(
        within = pe.PositiveReals, 
        doc = """Maximum volume of food consumed. 
        :math:`v^{max}`""")

    #--------------------------
    #       Variables
    #--------------------------

    m.x = Var(m.F, 
        within = pe.NonNegativeIntegers, 
        doc = """Number of servings consumed of each food. 
        :math:`x_f \\geq 0`""")

    #--------------------------
    #       Expressions
    #--------------------------

    m.total_volume = Expression(
        rule = lambda m: pe.summation(m.volume, m.x),
        doc = """Total volume of food consumed. \n
        .. math:: v^{tot} = \\sum_{f \\in \\mathcal{F}} 
            v_f \\cdot x_f""")

    m.intake = Expression(m.N,
        rule = lambda m,n: sum(m.content[f,n] * m.x[f] for f in m.F),
        doc = """Total intake of each nutrient. \n
        .. math:: y_n = \\sum_{f \\in \\mathcal{F}} 
            \\alpha_{f,n} \\cdot x_f""")

    #--------------------------
    #       Objective
    #--------------------------

    m.minimize_total_cost = Objective(
        rule = lambda m: pe.summation(m.cost, m.x), 
        doc = """Minimize the cost of food that is consumed. \n
        .. math:: \\min_{x} \\sum_{f \\in \\mathcal{F}} c_f \\cdot x_f""")

    #--------------------------
    #       Constraints
    #--------------------------

    m.nutrient_limit = Constraint(m.N, 
        rule = lambda m,n: inequality(m.min_intake[n], m.intake[n], m.max_intake[n]),
        doc = """Enforce upper and lower bounds on intake of each nutrient. \n
        .. math:: y^{min}_n \\leq y_n \\leq y^{max}_n""")

    m.volume_limit = Constraint(
        expr = m.total_volume <= m.max_volume, 
        doc = """Limit the volume of food consumed. \n
        .. math:: v^{tot} \\leq v^{max}""")

    return m