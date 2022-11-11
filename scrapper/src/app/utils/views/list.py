
from math import ceil

from . import GenericAPIView
from sanic.request import Request

class ListAPIView(GenericAPIView):
    """
        This class is used to list all the records
    """

    async def current_pagination(self, request: Request, *args, **kwargs):
        """
            This method is used to get the current pagination

            Args:
                request (Request): Sanic request object
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                tuple: Tuple of pagination (page, per_page)
            """
        page: int = int(request.args.get('page', 1))
        per_page: int = int(request.args.get('per_page', 20)) or 20
        return page, per_page

    async def get_records(self, *args, **kwargs):
        """
            This method is used to get all the records

            Args:
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                list: List of records
        """
        return []

    async def paginate(self, records:list , page, per_page):
        """
            This method is used to paginate the records

            Args:
                records (list): List of records
                page (int): Page number
                per_page (int): Per page number

            Returns:
                list: paginated records
        """
        return records[(page - 1) * per_page: page * per_page]

    async def get_total_records(self, records: list, *args, **kwargs):
        """
            This method is used to get the total number of records

            Args:
                records (list): List of records
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                int: Total number of records
        """
        return len(records)

    async def get_total_pages(self, records: list, per_page: int, *args, **kwargs):
        """
            This method is used to get the total number of pages

            Args:
                records (list): List of records
                per_page (int): Per page number
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                int: Total number of pages
        """
        return ceil(len(records) / per_page)

    async def make_body(self, request: Request, *args, **kwargs):
        """
            This method is used to make the body of the response

            Args:
                request (Request): Sanic request object
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: A dict of the body with data and pagination info
        """

        records: list = await self.get_records(*args, **kwargs)
        page, per_page = await self.current_pagination(request, *args, **kwargs)
        total_records: int = await self.get_total_records(records, *args, **kwargs)
        total_pages: int = await self.get_total_pages(records, per_page, *args, **kwargs)
        paginated_records: list = await self.paginate(records, page, per_page)

        return {
            'data': paginated_records,
            'pagination': {
                'total_records': total_records,
                'total_pages': total_pages,
                'per_page': per_page,
                'page': page,
                'next_page': page + 1 if page * per_page < total_records else total_pages,
                'prev_page': page - 1 if page > 1 else 1,

            }
        }

    async def get(self, request: Request, *args, **kwargs):
        """
            Template method to get all the records

            Args:
                request (Request): Sanic request object
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Response 200 success
        """

        body: dict = await self.make_body(request, *args, **kwargs)
        return self.success(data=body)
