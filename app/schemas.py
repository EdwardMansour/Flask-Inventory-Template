from marshmallow import fields, Schema

# This File is Serializer


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str(required=True)
    date_of_birth = fields.Date(required=True)
    role = fields.Str(required=True)


class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True)
    amount = fields.Str(required=True)
    expiry_date = fields.DateTime()
    is_destroyed = fields.Bool()
