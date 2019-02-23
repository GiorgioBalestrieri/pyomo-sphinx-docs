Tutorial
========

Follow the following steps:

- set up Sphinx *optional*
    - install Sphinx (pip or conda are very convenient) - 
    - initialize a docs folder (if not existing) by running :code:`sphinx-quickstart`
- create your Pyomo model
- generate model documentation
    - import your model and :func:`pyomo_sphinx_docs.get_pyomo_model_docs`
    - pass your model to :func:`pyomo_sphinx_docs.get_pyomo_model_docs` and get the .rst documentation as a string
    - save to file
- build your project documentation through Sphinx *optional*
    - add your file to the docs :code:`toctree`
    - create your documentation by running :code:`make html`

.. code-block:: python

    # import needed to create Pyomo model
    from diet import create_model

    from pyomo_sphinx_docs import get_pyomo_model_docs

    model = create_model() # create model

    docs = get_pyomo_model_docs(model) # get .rst docs as str

    # save to file
    with open("docs/diet_model.rst", "w") as f:
        f.write(docs)

In-line math
~~~~~~~~~~~~

For in-line math, use the :code:`:math:` directive.

Notice that since the docs are generated through strings, 
you need to escape backslashes, e.g. :code:`"\\alpha"`.

.. code-block:: python

    m.x = Var(m.F, 
        within = pe.NonNegativeIntegers, 
        doc = """Number of servings consumed of each food. 
        :math:`x_f \\geq 0`""")

Multi-line math
~~~~~~~~~~~~~~~

For math blocks, use the :code:`.. math::` directive.

A few notes:

- as all blocks directives, it must be preceded by an empty line. This can be achieved by adding an end-of-line character :code:`\n` at the end of the previous line.
- since the math block is a directive block, indentation matters: the math equation can be spread over multiple lines, but all lines after the first one must be indented.

.. code-block:: python

    m.total_volume = Expression(
        rule = lambda m: pe.summation(m.volume, m.x),
        doc = """Total volume of food consumed. \n
        .. math:: v^{tot} = \\sum_{f \\in \\mathcal{F}} 
            v_f \\cdot x_f""")