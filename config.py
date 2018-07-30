import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    FLASK_HOME = basedir
    FLASK_APP = os.path.join(FLASK_HOME, 'app.py')
    FLASK_DATALAYER = 'mysql+pymysql://root:123456@db/todolists'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    pass
