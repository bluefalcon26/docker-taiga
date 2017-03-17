# -*- coding: utf-8 -*-
# Copyright (C) 2014-2016 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2016 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2016 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2016 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .development import *

#########################################
## GENERIC
#########################################

#ADMINS = (
#    ("Admin", "example@example.com"),
#)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'taiga',
        'USER': 'taiga',
        'PASSWORD': 'thisisthetaigapassword',
        'HOST': 'postgres',
    }
}

SITES = {
    "api": {
       "scheme": "http",
       "domain": os.getenv("API_NAME"),
       "name": "api"
    },
    "front": {
       "scheme": "http",
       "domain": os.getenv("FRONT_NAME"),
       "name": "front"
    },
}

SITE_ID = "api"

MEDIA_ROOT = '/home/taiga/media'
STATIC_ROOT = '/home/taiga/static'

MEDIA_URL = "http://" + os.getenv("FRONT_NAME") + "/media/"
STATIC_URL = "http://" + os.getenv("FRONT_NAME") + "/static/"
ADMIN_MEDIA_PREFIX = "http://" + os.getenv("FRONT_NAME") + "/static/admin/"

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False
TEMPLATE_DEBUG = False


#########################################
## THROTTLING
#########################################

#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon": "20/min",
#    "user": "200/min",
#    "import-mode": "20/sec",
#    "import-dump-mode": "1/minute"
#}


#########################################
## MAIL SYSTEM SETTINGS
#########################################

DEFAULT_FROM_EMAIL = "system@" + os.getenv("FRONT_NAME")
SERVER_EMAIL = DEFAULT_FROM_EMAIL
#CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 #seconds

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS")
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# GMAIL SETTINGS EXAMPLE
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_USE_TLS = True
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_HOST_USER = 'youremail@gmail.com'
#EMAIL_HOST_PASSWORD = 'yourpassword'


#########################################
## REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = False

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
#USER_EMAIL_ALLOWED_DOMAINS = None

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
#MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
#MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
#MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
#MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit

# GITHUB SETTINGS
#GITHUB_URL = "https://github.com/"
#GITHUB_API_URL = "https://api.github.com/"
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"


#########################################
## SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
FEEDBACK_ENABLED = True
FEEDBACK_EMAIL = "support@taiga.io"


#########################################
## STATS
#########################################

STATS_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second


#########################################
## CELERY
#########################################

#from .celery import *
#CELERY_ENABLED = True
#
# To use celery in memory
#CELERY_ENABLED = True
#CELERY_ALWAYS_EAGER = True
