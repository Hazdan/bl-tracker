import json

from api.v1.books.models import Book
from app.utils.views import ListAPIView, CreateAPIView
from tortoise.contrib.pydantic import pydantic_queryset_creator

class BookListAPIView(ListAPIView):
    model = Book

    async def get_records(self):
        schema = pydantic_queryset_creator(self.model)
        instances = await schema.from_queryset(self.model.all())
        instances = json.loads(instances.json())
        return instances


class BookCreateAPIView(CreateAPIView):
    model = Book


class BookAPIView(BookCreateAPIView, BookListAPIView):
    pass