
class Config(object):
    DEBUG = False
    SECRET_KEY = 'Integrify'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ConfigPostgres(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/Todo'


class ConfigSqlite(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///todo.db"
    