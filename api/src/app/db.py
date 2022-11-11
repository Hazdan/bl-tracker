from tortoise.contrib.sanic import register_tortoise
from app.config import AppConfig


def make_conn(app: any) -> None:
    """
        This function is used to make the connection with the sql database

    Args:
        app (Sanic): Sanic app

    Returns:
        None
    """
    config = AppConfig()
    register_tortoise(
        app,
        config={
            'connections': {
                'default': {
                    'engine': 'tortoise.backends.mysql',
                    'credentials': {
                        'host': config.DB_HOST,
                        'port': config.DB_PORT,
                        'user': config.DB_USER,
                        'password': config.DB_PASSWORD,
                        'database': config.DB_NAME,
                    }
                },
            },
            'apps': {
                'models': {
                    'models': [
                        'api.v1.books.models',
                    ],
                    'default_connection': 'default',
                }
            }
        },
        generate_schemas=True
    )