import json

import logging

from app.models import Product
from datetime import datetime, timedelta
from flask_jwt_extended import create_access_token


def test_product_count(init_database):
    user_count = init_database.session.query(Product).count()
    assert user_count == 15, "There should be exactly 15 products in the database."


def test_create_product(client, init_database):

    access_token = create_access_token(identity=1)
    headers = {'Authorization': f'Bearer {access_token}'}

    data = {
        'name': 'Test Product',
        'amount': 10,
        'expiry_date': (datetime.now() + timedelta(days=10)).strftime('%Y-%m-%d')
    }

    response = client.post('/products', headers=headers, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.status_code == 200, f"Response data: {response.data}"


def test_update_product(client, init_database):

    access_token = create_access_token(identity=1)

    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        'name': 'Updated Product',
        'amount': 20,
        'expiry_date': (datetime.now() + timedelta(days=20)).strftime('%Y-%m-%d')
    }

    response = client.put('products/16', headers=headers, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200
    assert response.json['name'] == 'Updated Product'


def test_destroy_product(client, init_database):

    access_token = create_access_token(identity=1)

    headers = {'Authorization': f'Bearer {access_token}'}
    response = client.patch('products/16', headers=headers)

    assert response.status_code == 200
    assert response.json['is_destroyed'] is True


def test_get_all_products(client, init_database):

    access_token = create_access_token(identity=1)

    headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/products', headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json, list)

    assert len(response.json) == 6


def test_get_all_products_expired(client, init_database):

    access_token = create_access_token(identity=1)

    headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/products', headers=headers, query_string={'is_expired': 'true'})

    assert response.status_code == 200
    assert isinstance(response.json, list)

    assert len(response.json) == 1


def get_unexpired_products(client):

    access_token = create_access_token(identity=1)

    headers = {'Authorization': f'Bearer {access_token}'}
    response = client.get('/products', headers=headers, query_string={'is_expired': 'false'})

    assert response.status_code == 200
    assert isinstance(response.json, list)

    assert len(response.json) == 3


def test_prevent_update_other_user_product(client, init_database):
    access_token = create_access_token(identity=1)
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        'name': 'Updated Product',
        'amount': 20,
        'expiry_date': (datetime.now() + timedelta(days=20)).strftime('%Y-%m-%d')
    }

    response = client.put('/products/2', headers=headers, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 403, f"Expected status code 403, got {response.status_code}"
    assert response.json['message'] == 'Unauthorized: You are not the owner of this product'


def test_admin_update_other_user_product(client, init_database):

    access_token = create_access_token(identity=3)
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {
        'name': 'Admin Updated Product',
        'amount': 30,
        'expiry_date': (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
    }

    response = client.put('/products/1', headers=headers, data=json.dumps(data), content_type='application/json')

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert response.json['name'] == 'Admin Updated Product'
    assert response.json['amount'] == 30
    assert response.json['expiry_date'] == (datetime.now() + timedelta(days=30)).strftime('%Y-%m-%d')
