from tortoise import Model, fields


class Book(Model):
    id = fields.IntField(pk=True)
    title = fields.CharField(max_length=255)
    url = fields.CharField(max_length=255)
    img = fields.CharField(max_length=255, null=True)

    class Meta:
        table = 'books'