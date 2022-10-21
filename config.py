
class Config(object):
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # Token secret key
    SECRET_KEY = 'Integrify'
    # Token expire time in minutes
    TOKEN_EXP = 30

class ConfigPostgres(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1234@localhost/Todo'


class ConfigSqlite(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///todo.db"
    