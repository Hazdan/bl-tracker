from requests import Response
from requests_html import HTML, AsyncHTMLSession


class GenericDataMiner:

    def __init__(self):
        self.session = AsyncHTMLSession()

    async def get_html(self, url: str, *args, **kwargs) -> HTML:
        """
            This method is used to get data from the response

            Args:
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Data from the response
        """
        response: Response = await self.session.get(url)
        return response.html

    async def extract_data(self, data, *args, **kwargs) -> dict:
        """
            This method is used to extract data from the response

            Args:
                response (dict): Response from the session to get data
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Data from the response
        """

        return {}


    async def parse_data(self, data, *args, **kwargs) -> list:
        """
            This method is used to parse data from the response

            Args:
                data (dict): Data extracted from the response
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Data from the response
        """
        return data

    async def mine(self, url: str, *args, **kwargs) -> list:
        """
            This method is used to mine data from the url

            Args:
                url (str): Url to mine data from
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Parsed data from the response
        """
        html: HTML = await self.get_html(url, *args, **kwargs)
        data: dict = await self.extract_data(html, *args, **kwargs)
        parsed_data: list = await self.parse_data(data, *args, **kwargs)
        return parsed_data
