from api.v1.books.views import BookAPIView
from sanic import Blueprint


books = Blueprint('books', url_prefix='/books', strict_slashes=False)

books.add_route(BookAPIView.as_view(), '/')