from datetime import datetime

import pytest
from app.models import User


def test_user_count(init_database):
    user_count = init_database.session.query(User).count()
    assert user_count == 3, "There should be exactly 3 users in the database."


@pytest.mark.usefixtures('init_database')
def test_register(init_database, client):
    data = {
        "username": "test_user",
        "password": "test_password",
        "date_of_birth": "1990-01-01"
    }
    response = client.post('/register', json=data)
    user_count = init_database.session.query(User).count()
    assert response.status_code == 200
    assert response.json['username'] == 'test_user'
    assert response.json['date_of_birth'] == '1990-01-01'
    assert user_count == 4, "There should be exactly 4 users in the database."


def test_login(init_database, client):
    data = {
        "username": "edward",
        "password": "Pass1234"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 200
    assert 'access_token' in response.json


def test_login_admin(init_database, client):
    data = {
        "username": "admin",
        "password": "Pass1234"
    }
    response = client.post('/login', json=data)
    assert response.status_code == 200
    assert 'access_token' in response.json


@pytest.mark.usefixtures('init_database')
def test_register_error_already_exist_user(init_database, client):
    data = {
        "username": "test_user",
        "password": "test_password",
        "date_of_birth": "1990-01-01"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400
    assert response.json == {'username': ['Username already exists.']}


@pytest.mark.usefixtures('init_database')
def test_register_error_date_of_birth(init_database, client):
    data = {
        "username": "test_user_test_2",
        "password": "test_password",
        "date_of_birth": f"{datetime.now().year + 1}-01-01"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400
    assert response.json == {'date_of_birth': ["Date of birth can't be in the future."]}


@pytest.mark.usefixtures('init_database')
def test_register_error_date_of_birth(init_database, client):
    data = {
        "username": "test_user_test_2",
        "password": "test_password",
        "date_of_birth": f"{datetime.now().year - 110}-01-01"
    }
    response = client.post('/register', json=data)
    assert response.status_code == 400
    assert response.json == {'date_of_birth': ["Date of birth can't be before 1924, hello from underground."]}