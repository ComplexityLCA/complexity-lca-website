# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Complexity-LCA'
# copyright = '2024, Gustavo Larrea, Tomas Navarrete'
# author = 'Gustavo Larrea, Tomas Navarrete'
# release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
'myst_parser',
'sphinxcontrib.bibtex',
]

bibtex_bibfiles = ['bibliography.bib']

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_book_theme'
html_context = {
   "default_mode": "light",
    "reading_mode": "light"
}


html_static_path = ['_static']
