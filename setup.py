from setuptools import setup, find_packages
from os import path
from io import open

_here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(_here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyomo_sphinx_docs',
    version='0.1.0',
    description=('Create Sphinx documentation from Pyomo models.'),
    author='Giorgio Balestrieri',
    author_email='gbalestrieri@tesla.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=['pyomo', 'sphinx']
    )