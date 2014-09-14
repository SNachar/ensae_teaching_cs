#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Présentation documentation build configuration file, created by
# sphinx-quickstart on Sat Feb  1 15:52:14 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os


# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinxjp.themes.revealjs',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'ENSAE 2A - Données, Machine Learning et Programmation'
copyright = '2014, ENSAE'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.5'
# The full version, including alpha/beta/rc tags.
release = '0.5'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all
# documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
#keep_warnings = False


# -- Options for HTML output ----------------------------------------------

html_theme_options = {

    # Set the lang attribute of the html tag. Defaults to "ja"
    "lang": "fr",

    # The "normal" size of the presentation, aspect ratio will be preserved
    # when the presentation is scaled to fit different resolutions
    "width": 1076,
    "height": 750,

    # Factor of the display size that should remain empty around the content
    "margin": 0.1,

    # Bounds for smallest/largest possible scale to apply to content
    "min_scale": 0.2,
    "max_scale": 1.0,

    # Display controls in the bottom right corner
    "controls": True,

    # Display a presentation progress bar
    "progress": True,

    # Push each slide change to the browser history
    "history": False,

    # Enable keyboard shortcuts for navigation
    "keyboard": True,

    # Enable the slide overview mode
    "overview": True,

    # Vertical centring of slides
    "center": True,

    # Enables touch navigation on devices with touch input
    "touch": True,

    # Loop the presentation
    "loop": False,

    # Change the presentation direction to be RTL
    "rtl": False,

    # Turns fragments on and off globally
    "fragments": True,

    # Number of milliseconds between automatically proceeding to the
    # next slide, disabled when set to 0, this value can be overwritten
    # by using a data-autoslide attribute on your slides
    "auto_slide": 0,

    # Enable slide navigation via mouse wheel
    "mouse_wheel": True,

    # Apply a 3D roll to links on hover
    "rolling_links": True,

    # Opens links in an iframe preview overlay
    "preview_links": True,

    # Theme (default/blood/beige/moon/night/serif/simple/sky/solarized)
    "theme": "solarized",

    # Transition style (default/cube/page/concave/zoom/linear/fade/none)
    "transition": "linear",

    # Transition speed (default/fast/slow)
    "transition_speed": "default",

    # Transition style for full page slide backgrounds (default/linear)
    "background_transition": "default",

    # Display the page number of the current slide
    "slide_number": True,

    # Flags if the presentation is running in an embedded mode,
    # i.e. contained within a limited portion of the screen
    "embedded": False,

    # Stop auto-sliding after user input
    "auto_slide_stoppable": True,

    # Hides the address bar on mobile devices
    "hide_address_bar": True,

    # Parallax background image
    # CSS syntax, e.g. "a.jpg"
    "parallax_background_image": '', #a.jpg',

    # Parallax background size
    # CSS syntax, e.g. "3000px 2000px"
    "parallax_background_size": '', #3000px 2000px',

    # Focuses body when page changes visibility to ensure keyboard shortcuts work
    "focus_body_on_page_visibility_change": True,

    # Number of slides away from the current that are visible
    "view_distance": 3,

    # Enable plugin javascript for reveal.js
    "plugin_list": [
        "_static/plugin/leap/leap.js",
        "_static/plugin/multiplex/master.js",
        #"_static/plugin/search/search.js",
        "_static/plugin/remotes/remotes.js"
        "_static/plugin/notes-server/client.js",
        "_static/plugin/math/math.js",
    ],

    "math": {
        "mathjax": 'http://cdn.mathjax.org/mathjax/latest/MathJax.js',
        # See http://docs.mathjax.org/en/latest/config-files.html
        "config": 'TeX-AMS_HTML-full'
    },
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'revealjs'
html_use_index = False

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/project_ico.ico"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'ensae_1a'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
  ('index', 'ensae_1a.tex', 'ENSAE 1A Programmation',
   'Xavier Dupré', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'presentation', 'Présentation Documentation',
     ['Xavier Dupré'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Prsentation', 'Présentation Documentation',
   'ENSAE', 'ensae_2a', 'Présentation du cours, ENSAE 2A - Données, Machine Learning et Programmation',
   '1h'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#texinfo_no_detailmenu = False
