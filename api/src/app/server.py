from api import api
from sanic import Sanic

from app.db import make_conn


def create_app(config: any) -> Sanic:
    """
        This function is used to create the sanic app
    Returns:
        Sanic: Sanic app
    """
    app = Sanic("main", config=config, strict_slashes=False)
    app.blueprint(api)
    make_conn(app)
    return app