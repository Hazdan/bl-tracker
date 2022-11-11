from sanic import Blueprint

from .books import books_bp


api_bp = Blueprint.group((books_bp,), url_prefix='/', strict_slashes=False)
