import sys
import os
import pytest

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

from app import create_app, db

@pytest.fixture(scope="session")
def app():
    app = create_app(testing=True)

    # Application context is needed for DB operations
    with app.app_context():
        yield app


@pytest.fixture(scope="session")
def client(app):
    return app.test_client()


@pytest.fixture(scope="function")
def db_session(app):
    """
    Provides a clean database for each test.
    """
    with app.app_context():
        db.create_all()
        yield db
        db.session.remove()
        db.drop_all()

