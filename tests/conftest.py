import pytest
from sqlalchemy import text
from app import create_app, db
from config import TestConfig
import logging

logging.basicConfig(level=logging.INFO)


@pytest.fixture(scope='module')
def app():
    _app = create_app(TestConfig)
    with _app.app_context():
        db.create_all()
        yield _app
        db.drop_all()


@pytest.fixture(scope='module')
def init_database(app):
    with app.app_context():
        # Load test data
        with open('tests/data/test_db.sql', 'r') as f:
            sql_statements = f.read().split(';')
            for statement in sql_statements:
                if statement.strip():
                    db.session.execute(text(statement))
            db.session.commit()

        yield db


@pytest.fixture
def client(app, init_database):
    with app.test_client() as test_client:
        yield test_client
