from sanic.config import Config


class BaseConfig(Config):

    # --------- SANIC ---------
    HOST = '0.0.0.0'
    PORT = 3000
    DEBUG = True
    AUTO_RELOAD = True

     # --------- DATABASE ---------

    DB_HOST = '172.21.0.2'
    DB_PORT = '3306'
    DB_USER = 'root'
    DB_PASSWORD = 'root'
    DB_NAME = 'bltrack'


try:
    from app.local_settings import ProductionConfig as BaseConfig
except ImportError:
    try:
        from app.local_settings import DevelopmentConfig as BaseConfig
    except ImportError:
        pass


class AppConfig(BaseConfig):
    pass