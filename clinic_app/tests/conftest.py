import sys
import os
import pytest

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, BASE_DIR)

from app import create_app, db

@pytest.fixture
def app():
    os.environ["FLASK_ENV"] = "testing"
    app = create_app(testing=True)
    return app


@pytest.fixture
def client(app):
    return app.test_client()














