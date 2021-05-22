#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Sophia Booth Magnone'
SITENAME = 'Sophia Booth Magnone'
SITESUBTITLE = 'Grant Writing Consultant'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10
PAGINATED_TEMPLATES = {'index': None, 'tag': None, 'category': None, 'author': None}

USE_FOLDER_AS_CATEGORY = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = './theme/'

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_PATHS = ['']
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
INDEX_SAVE_AS = 'blog/index.html'

STATIC_PATHS = ['images', 'pdfs', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

import datetime  # noqa
BUILD_TIME = datetime.datetime.now().year
