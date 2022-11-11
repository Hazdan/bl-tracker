from api.books.views import BooksCreateAPIView
from sanic import Blueprint

books_bp = Blueprint('books', url_prefix='/books', strict_slashes=False)

books_bp.add_route(BooksCreateAPIView.as_view(), '/')
