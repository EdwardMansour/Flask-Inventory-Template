from flasgger import swag_from
from datetime import datetime

from flask import request, jsonify

from . import api_bp
from app.services import create_user, authenticate_user
from app.schemas import UserSchema, RegisterUserSchema
from flask_jwt_extended import create_access_token


@api_bp.route('/register', methods=['POST'])
@swag_from('../../swagger_docs/user_register.yaml')
def register():
    data = request.get_json()

    register_user_schema = RegisterUserSchema()
    errors = register_user_schema.validate(data)

    if errors:
        return jsonify(errors), 400

    user = create_user(data['username'], data['password'], datetime.strptime(data['date_of_birth'], '%Y-%m-%d'))
    user_schema = UserSchema()
    serialized_user = user_schema.dump(user)
    return jsonify(serialized_user)


@api_bp.route('/login', methods=['POST'])
@swag_from('../../swagger_docs/login.yaml')
def login():
    data = request.get_json()
    user = authenticate_user(data['username'], data['password'])
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401
