#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

# NOTE: This file borrows *heavily* from the config file of Jake
#       Vanderplas' blog:https://github.com/jakevdp/PythonicPerambulations.git


AUTHOR = u'EconForge'
SITENAME = u'EconForge'
SITESUBTITLE = u'Where economists come for code'
TAGLINE = u'Where economists come for code'
SITEURL = 'http://www.econforge.org'

PATH = 'content'

DEFAULT_DATE_FORMAT = '%b %d, %Y'
TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Set URLs
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# This requires Pelican 3.3+
STATIC_PATHS = ['images', 'figures', 'downloads', 'css', 'favicon.ico']
EXTRA_HEADER = open('_nb_javascript.html').read().decode('utf-8')

CODE_DIR = 'downloads/code'
NOTEBOOK_DIR = 'downloads/notebooks'

# Theme and plugins
THEME = 'themes/pure'
# THEME = 'themes/pelican-octopress-theme'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'liquid_tags.literal',
           'gravatar']

SOCIAL = (
    ('github', 'https://github.com/EconForge'),
    ('google', 'https://groups.google.com/forum/#!forum/econforge'),
)

DISPLAY_PAGES_ON_MENU = True

# Search
SEARCH_BOX = True
