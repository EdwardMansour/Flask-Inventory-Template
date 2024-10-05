from datetime import datetime

from flask import request, jsonify
from . import api_bp
from app.services import create_user, authenticate_user
from app.schemas import UserSchema
from flask_jwt_extended import create_access_token


@api_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    date_string = data['date_of_birth']
    date_format = "%Y-%m-%d"

    date_object = datetime.strptime(date_string, date_format)
    user = create_user(data['username'], data['password'], date_object)
    user_schema = UserSchema()
    serialized_user = user_schema.dump(user)
    return jsonify(serialized_user)


@api_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = authenticate_user(data['username'], data['password'])
    if user:
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad username or password"}), 401
