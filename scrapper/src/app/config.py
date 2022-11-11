from sanic.config import Config


class BaseConfig(Config):

    # --------- SANIC ---------
    HOST = '0.0.0.0'
    PORT = 3000
    DEBUG = True
    AUTO_RELOAD = True


try:
    from app.local_settings import ProductionConfig as BaseConfig
except ImportError:
    try:
        from app.local_settings import DevelopmentConfig as BaseConfig
    except ImportError:
        pass


class AppConfig(BaseConfig):
    pass
