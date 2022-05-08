from tortoise.models import Model
from tortoise import fields


class Model(Model):
    id = fields.IntField(pk=True)
    some_column = fields.CharField(max_length=69)
