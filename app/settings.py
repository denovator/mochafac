# -*- coding: utf-8 -*-
from datetime import timedelta


class Config(object):
    SECRET_KEY = "asdfjlsadjflkjlwkqjerljlasdjfl"
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "seunghojung0114@gmail.com"
    SQLALCHEMY_DATABASE_URI = "mysql+gaerdbms:///flaskr?instance=mochafac:flaskr-instance"
    migration_directory = "migrations"
