import json

from tortoise.contrib.pydantic import pydantic_model_creator

from . import GenericAPIView


class CreateAPIView(GenericAPIView):
    """
        This class is used to create a record
    """

    async def post(self, request: any) -> dict:
        data = request.json or request.form
        try:
            instance = await self.model.create(**data)
        except Exception as e:
            return await self.bad_request(f'{e}')

        schema = pydantic_model_creator(self.model)
        instance = await schema.from_tortoise_orm(instance)
        
        return await self.created(json.loads(instance.json()))

        return await self.created()