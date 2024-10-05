from enum import Enum

from flask_bcrypt import generate_password_hash, check_password_hash

from app import db


class UserRole(Enum):
    ADMIN = 'admin'
    REGULAR = 'regular'


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    date_of_birth = db.Column(db.Date(), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.REGULAR, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    is_destroyed = db.Column(db.Boolean, default=False, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expiry_date = db.Column(db.Date(), nullable=True)



