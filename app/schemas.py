from marshmallow import fields, Schema, validate, ValidationError

from app.validators import validate_date, validate_expiry_date, validate_unique_username


# This File is Serializer


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str(required=True)
    date_of_birth = fields.Date(required=True)
    role = fields.Str(required=True)


class RegisterUserSchema(Schema):
    username = fields.Str(required=True,
                          validate=validate.And(validate.Length(min=1, max=80), validate_unique_username))
    password = fields.Str(required=True, validate=validate.Length(min=6, max=36))
    date_of_birth = fields.Str(required=True, validate=validate_date)


class ProductSchema(Schema):
    id = fields.Int()
    name = fields.Str(required=True, validate=validate.Length(min=1, max=80))
    amount = fields.Float(required=True, validate=validate.Range(min=0.1))
    expiry_date = fields.DateTime()
    is_destroyed = fields.Bool(validate=validate.OneOf([True, False]))


class CreateProductSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=80))
    amount = fields.Float(required=True, validate=validate.Range(min=0.1))
    expiry_date = fields.Str(required=True, validate=validate_expiry_date)


class UpdateProductSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1, max=80))
    amount = fields.Float(required=True, validate=validate.Range(min=0.1))
    expiry_date = fields.Str(required=True, validate=validate_expiry_date)
