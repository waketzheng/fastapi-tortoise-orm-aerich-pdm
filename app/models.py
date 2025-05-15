from tortoise import Model, fields


class Users(Model):
    name = fields.CharField(max_length=20)
