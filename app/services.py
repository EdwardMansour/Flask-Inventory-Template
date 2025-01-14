from datetime import datetime

from app import db
from app.models import User, Product


def create_superuser(username, password, date_of_birth):
    user = User(username=username, date_of_birth=datetime.strptime(date_of_birth, "%Y-%m-%d"), role='ADMIN')
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user


def create_user(username, password, date_of_birth):
    user = User(username=username, date_of_birth=date_of_birth)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user


def authenticate_user(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        return user
    return None


def create_product(user_id, name, amount, expiry_date):
    product = Product(name=name, amount=amount, user_id=user_id, expiry_date=expiry_date)
    db.session.add(product)
    db.session.commit()
    return product


def update_product(product_id, name, amount, expiry_date):
    product = db.session.get(Product, product_id)

    if product:
        product.name = name
        product.amount = amount
        product.expiry_date = expiry_date
        db.session.commit()
    return product


def destroy_product(product_id):
    product = db.session.get(Product, product_id)

    if product:
        product.is_destroyed = True
        db.session.commit()
    return product
