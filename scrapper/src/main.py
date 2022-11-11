from app.server import create_app
from app.config import AppConfig


if __name__ == '__main__':
    config = AppConfig()
    app = create_app(config)
    app.run(
        host=config.HOST,
        port=config.PORT,
        debug=config.DEBUG,
        auto_reload=config.AUTO_RELOAD
    )
