from flasgger import swag_from
from datetime import date, datetime

from flask import request, jsonify
from . import api_bp
from app.services import create_product, update_product, destroy_product
from app.schemas import ProductSchema, CreateProductSchema, UpdateProductSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models import Product, User, UserRole


@api_bp.route('/products', methods=['POST'])
@jwt_required()
@swag_from('../../swagger_docs/create_product.yaml')
def create():
    data = request.get_json()  # get body from request
    user_id = get_jwt_identity()
    create_product_schema = CreateProductSchema()
    errors = create_product_schema.validate(data)

    if errors:
        return jsonify(errors), 400

    product = create_product(user_id, data['name'], data['amount'], datetime.strptime(data['expiry_date'], '%Y-%m-%d'))
    product_schema = ProductSchema()
    serialized_product = product_schema.dump(product)
    return jsonify(serialized_product), 200


@api_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
@swag_from('../../swagger_docs/update_product.yaml')
def update(product_id):
    user_id = get_jwt_identity()
    product = Product.query.get(product_id)
    user = User.query.get(user_id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404
    if user.role != UserRole.ADMIN and product.user_id != user_id:
        return jsonify({"message": "Unauthorized: You are not the owner of this product"}), 403

    data = request.get_json()

    upgrade_product_schema = UpdateProductSchema()
    errors = upgrade_product_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    product = update_product(product_id, data['name'], data['amount'],
                             datetime.strptime(data['expiry_date'], '%Y-%m-%d'))
    product_schema = ProductSchema()
    serialized_product = product_schema.dump(product)
    return jsonify(serialized_product), 200


@api_bp.route('/products/<int:product_id>', methods=['PATCH'])
@jwt_required()
@swag_from('../../swagger_docs/destroy_product.yaml')
def destroy(product_id):
    user_id = get_jwt_identity()
    product = Product.query.get(product_id)
    user = User.query.get(user_id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    if user.role != UserRole.ADMIN and product.user_id != user_id:
        return jsonify({"message": "Unauthorized: You are not the owner of this product"}), 403

    product = destroy_product(product_id)
    product_schema = ProductSchema()
    serialized_product = product_schema.dump(product)

    return jsonify(serialized_product), 200


@api_bp.route('/products', methods=['GET'])
@jwt_required()
@swag_from('../../swagger_docs/get_products.yaml')
def get_all():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    expired = request.args.get('is_expired', default=None)
    if expired == 'true':
        is_expired = True
    elif expired == 'false':
        is_expired = False
    else:
        is_expired = None

    query = Product.query

    if user.role != UserRole.ADMIN:
        query = query.filter_by(user_id=user_id)

    if is_expired:
        query = query.filter((Product.expiry_date <= date.today()) | Product.is_destroyed)
    elif is_expired == False:
        query = query.filter(Product.expiry_date > date.today()).filter(Product.is_destroyed == False)

    products = query.all()
    products_schema = ProductSchema(many=True)
    return jsonify(products_schema.dump(products)), 200
