# coding: utf-8


class Configuration(object):
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:123456@localhost/bell_station")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # REDIS_OPTIONS = {
    #     "host": "localhost",
    # }
    SECRET_KEY = "secret_key"
    DEBUG = True
    REDIS_PREFIX = "bell_station"
