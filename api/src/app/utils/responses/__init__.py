from sanic.response import json

class Responses:

    async def success(
        self,
        data: dict = {},
    ) -> dict:
        """
            Return success response

            Args:
                data (dict, optional): Data to be returned. Defaults to {}.

            Returns:
                dict: Success response 200
        """

        return json(
            body=data,
            status=200,
        )

    async def created(
        self,
        data: dict = {},
    ) -> dict:
        """
            Return created response

            Args:
                data (dict, optional): Data to be returned. Defaults to {}.

            Returns:
                dict: Created response 201
        """

        return json(
            body=data,
            status=201,
        )
    
    async def bad_request(
            self,
            descripton: str = 'The request cannot be fulfilled due to bad syntax.'
    ) -> dict:
        """
            Return bad request response

            Args:
                descripton (str, optional): Description of the error. Defaults to 'The request cannot be fulfilled due to bad syntax'.

            Returns:
                dict: Bad request response 400
        """

        return json(
            body={
                'status': 400,
                'message': 'Bad request',
                'description': descripton
            },
            status=405,
        )

    async def not_found(
            self,
            descripton: str = 'The requested resource was not found'
    ) -> dict:
        """
            Return not found response

            Args:
                descripton (str, optional): Description of the error. Defaults to 'The requested resource was not found'.

            Returns:
                dict: Not found response 404
        """
        return json(
            body={
                'status': 404,
                'message': 'Not Found',
                'description': descripton
            },
            status=404,
        )

    async def not_allowed(
            self,
            descripton: str = 'The requested resource is not allowed'
    ) -> dict:
        """
            Return not allowed response

            Args:
                descripton (str, optional): Description of the error. Defaults to 'The requested resource is not allowed'.

            Returns:
                dict: Not allowed response 405
        """

        return json(
            body={
                'status': 405,
                'message': 'Method Not Allowed',
                'description': descripton
            },
            status=405,
        )