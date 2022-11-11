import re
from datetime import datetime

from . import GenericDataMiner


class BuscalibreDataMiner(GenericDataMiner):

    @staticmethod
    async def format_date(date: str, input_format: str, output_format: str) -> str:
        try:
            date: datetime = datetime.strptime(date, input_format)
            date: str = date.strftime(output_format)
        except:
            date = None
        return date


    async def extract_data(self, data, *args, **kwargs):
        await data.arender(timeout=2)
        try:
            book_div = data.find('#producto', first=True)
            book = {}

            book['id'] = book_div.find('#addToCart', first=True).attrs.get('data-idproducto')
            book['title'] = book_div.find('.tituloProducto', first=True).text
            book['img'] = book_div.find('img', first=True).attrs.get('src')
            book['autor'] = book_div.find('.font-color-bl.link-underline', first=True).text
            book['price'] = int(book_div.find('.precioAhora', first=True).text.replace('$', '').replace('.', ''))
            return book
        except Exception as e:
            return False
