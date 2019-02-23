How to use
==========

This relies on `Sphinx <http://www.sphinx-doc.org/>`_.
See the Sphinx documentation, in particular installation, quickstart and reStructuredText.

.. note:: 
    Sphinx is not actually necessary for this to work. If you are happy having your documentation in reStructuredText, and you have other ways to generate html or other file formats from it, then you can skip some steps in the tutorial.
    Using Sphinx is recommended due to its power, simplicity and the fact that this will allow you to integrate your model documentation in the documentation of the code around it.

The approach is to use the :code:`doc` field of Pyomo components. 
The main benefit is that code and documentation can live together, making it much easier to keep them synced and to check that the documentation corresponds to the actual implementation.

This also comes with some limitations, namely:

- it relies on the model actually being built, meening it needs all the dependencies to be installed.
- for :code:`ConcreteModel` s that require data to be created, it will also require having access to such data and loading them.

