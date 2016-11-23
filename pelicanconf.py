#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Markus Sinnl'
SITENAME = 'Markus Sinnl'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS=['images','pdfs']
THEME='../pelican-themes/pelican-bootstrap3/'


# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter','https://twitter.com/msinnl'),
        ('github', 'http://github.com/msinnl'),
        ('google scholar', 'https://scholar.google.at/citations?user=aaw54NIAAAAJ&hl=de&oi=ao','fa-google'),
        ('ORCID','http://orcid.org/0000-0003-1439-8702'),
        ('researchgate','https://www.researchgate.net/profile/Markus_Sinnl')
      )

DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
        ('About', '/'),
        ('Publications', '/pages/publications.html'),
        ('Instances/Codes', '/pages/instancescodes.html'),
        ('Activities', '/pages/activities.html'),
        ('Talks', '/pages/talks.html'),
        ('Teaching', '/pages/teaching.html'),
        )


EMAIL = 'markus.sinnl (at) univie.ac.at'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
