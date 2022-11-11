from . import GenericAPIView

class CreateAPIView(GenericAPIView):
    """
        This class is used to create a record
    """

    async def post(self, request: any) -> dict:
        """
            This function create a new instance of the model
        Args:
            request (request): Request object
        Returns:
            dict: Return json with the created instance of the model
        """

        return await self.created()