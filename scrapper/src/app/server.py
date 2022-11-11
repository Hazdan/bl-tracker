from api import api_bp
from sanic import Sanic, response

from app.config import AppConfig


def create_app(config: AppConfig) -> Sanic:
    """
        This function is used to create the sanic app

    Returns:
        Sanic: Sanic app
    """
    app = Sanic("ScrapperBuscalibreTrack", config=config, strict_slashes=False)

    @app.get("/")
    async def index(request):
        return response.html('<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Document</title></head><body><form action="/books" method="POST"><input type="text" name="book_url"><input type="submit" value="Buscar..."></form></body></html>')

    app.blueprint(api_bp)


    return app
