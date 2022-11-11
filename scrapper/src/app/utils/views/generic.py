from sanic.views import HTTPMethodView
from app.utils.responses import Responses
from sanic.request import Request

class GenericAPIView(HTTPMethodView, Responses):
    """
        This class is used to create generic api view
    """

    def get(self, request: Request, *args, **kwargs):
        """
            Http get method

            Args:
                request (obj): Sanic request object
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Response 405 not allowed
        """
        return self.not_allowed()

    def post(self, request: Request, *args, **kwargs):
        """
            Http post method

            Args:
                request (obj): Sanic request object
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Response 405 not allowed
        """
        return self.not_allowed()

    def put(self, request: Request, *args, **kwargs):
        """
            Http put method

            Args:
                request (obj): Sanic request object
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Response 405 not allowed
        """
        return self.not_allowed()

    def patch(self, request: Request, *args, **kwargs):
        """
            Http patch method

            Args:
                request (obj): Sanic request object
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Response 405 not allowed
        """
        return self.not_allowed()

    def delete(self, request: Request, *args, **kwargs):
        """
            Http delete method

            Args:
                request (obj): Sanic request object
                *args (tuple): Tuple of args
                **kwargs (dict): Dict of kwargs

            Returns:
                dict: Response 405 not allowed
        """
        return self.not_allowed()

