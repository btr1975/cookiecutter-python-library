# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
base_path = os.path.split(os.path.join(os.path.abspath(os.path.dirname(__name__))))[0]
sys.path.append(base_path)
about = {}
with open(os.path.join(base_path, '{{cookiecutter.__library_name}}', 'version.py'), 'r', encoding='utf-8') as f:
    exec(f.read(), about)

{% if cookiecutter.library_documents_location == 'readthedocs.io' %}
# -- Added for readthedocs.org -----------------------------------------------

master_doc = 'index'
{% endif %}

# -- Project information -----------------------------------------------------

release = about['__version__']
project = f'{about["__title__"]} v{release}'
copyright = about['__copyright__']
author = about['__author__']


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.autodoc',
              'myst_parser',
              'docxsphinx',
              'sphinxcontrib.mermaid',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = '{{ cookiecutter.library_documents_theme }}'
if html_theme == 'alabaster':
    html_theme_options = {
        'description': f'{about["__description__"]}',
        'page_width': '95%',
        'body_max_width': '95%',
        'fixed_sidebar': 'true',
        'github_banner': 'true',
        'github_user': '{{ cookiecutter.git_username }}',
        'github_repo': about["__title__"]
    }
elif html_theme == 'sphinx_rtd_theme':
    html_theme_options = {
        # 'analytics_id': 'G-XXXXXXXXXX',
        # 'analytics_anonymize_ip': False,
        'logo_only': False,
        'display_version': True,
        'prev_next_buttons_location': 'bottom',
        'style_external_links': False,
        'vcs_pageview_mode': '',
        'style_nav_header_background': '#2980B9',
        # Toc options
        'collapse_navigation': True,
        'sticky_navigation': True,
        'navigation_depth': 4,
        'includehidden': True,
        'titles_only': False
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# This is used fpr making a PDF using rinohtype
# See https://www.mos6581.org/rinohtype/master/sphinx.html
rinoh_documents = [{'doc': 'index', 'target': f'{about["__title__"]}'}]

# This is used for render markdown using myst-parser
# see https://www.sphinx-doc.org/en/master/usage/markdown.html
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
