from app.utils.views import CreateAPIView
from app.utils.miners import BuscalibreDataMiner


class BooksCreateAPIView(CreateAPIView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.miner = BuscalibreDataMiner()

    async def post(self, request: any) -> dict:
        """
            This function create a new instance of the model
        Args:
            request (request): Request object
        Returns:
            dict: Return json with the created instance of the model
        """

        try:
            data = request.form

        except Exception as e:
            data = request.json

        data = request.form
        book = await self.miner.mine(data.get('book_url'))
        
        return await self.created({'book': book})