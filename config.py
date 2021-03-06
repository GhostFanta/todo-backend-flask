import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    FLASK_HOME = basedir
    FLASK_APP = os.path.join(FLASK_HOME, 'app.py')
    FLASK_DATALAYER = 'mysql+pymysql://root:123456@localhost/todolists'


class ProdConfig(Config):
    FLASK_DATALAYER = 'mysql+pymysql://root:123456@data/todolists'


class DevConfig(Config):
    pass
