from api.v1.books import books
from sanic import Blueprint

v1 = Blueprint.group(
    [
        books,
    ], version=1
)