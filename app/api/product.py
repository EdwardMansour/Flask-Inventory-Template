from datetime import date

from flask import request, jsonify
from . import api_bp
from app.services import create_product, update_product, destroy_product
from app.schemas import ProductSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models import Product, User

product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


@api_bp.route('/products', methods=['POST'])
@jwt_required()
def create():
    data = request.get_json()  # get body from request
    user_id = get_jwt_identity()
    product = create_product(user_id, data['name'], data['amount'])
    return product_schema.jsonify(product), 200


@api_bp.route('/products/<int:product_id>', methods=['PUT'])
@jwt_required()
def update(product_id):
    user_id = get_jwt_identity()
    product = Product.query.get(product_id)
    user = User.query.get(user_id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404
    if user.role != 'admin' and product.user_id != user_id:
        return jsonify({"message": "Unauthorized: You are not the owner of this product"}), 403

    data = request.get_json()
    expiry_date = None
    if user.role == 'admin' and data['expiry_date']:
        expiry_date = data['expiry_date']
    product = update_product(product_id, data['name'], data['amount'], expiry_date)
    return product_schema.jsonify(product)


@api_bp.route('/products/<int:product_id>', methods=['PATCH'])
@jwt_required()
def destroy(product_id):
    user_id = get_jwt_identity()
    product = Product.query.get(product_id)
    user = User.query.get(user_id)

    if product is None:
        return jsonify({"message": "Product not found"}), 404

    if user.role != 'admin' and product.user_id != user_id:
        return jsonify({"message": "Unauthorized: You are not the owner of this product"}), 403

    destroy_product(product_id)
    return jsonify({"msg": "Product Destroyed"}), 200


@api_bp.route('/products', methods=['GET'])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    is_expired = request.args.get('is_expired', type=bool)

    query = Product.query
    if user.role != 'admin':
        query = query.filter_by(user_id=user_id)

    if is_expired:
        query = query.filter((Product.expiry_date <= date.today()) | Product.is_destroyed)

    products = query.all()
    return jsonify(products_schema.dump(products)), 200
