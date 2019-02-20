#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Araras makers'
SITENAME = 'Arara Makerspace'
SITEURL = 'https://araramakerspace.github.io/blog/'

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'en'

THEME = 'pelican-themes/pelican-blue'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10


SIDEBAR_DIGEST = 'Arara makerspace the best place in the world'

FAVICON = 'url-to-favicon'

DISPLAY_PAGES_ON_MENU = True

TWITTER_USERNAME = 'twitter-user-name'

MENUITEMS = (('Blog', SITEURL),('Home', SITEURL),('Help-us', SITEURL))

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
