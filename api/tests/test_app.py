# tests/test_app.py
import os
import pytest
from flask import Flask
from api.app import create_app
from api.db import db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    # Set a different database URL for testing
    test_db_url = 'sqlite:///:memory:'
    
    app = create_app(test_db_url)
    app.config['TESTING'] = True

    # Create the database and the database table
    with app.app_context():
        db.create_all()

    yield app

    # Teardown the database
    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_app_config(app):
    """Test app configuration."""
    assert app.config['API_TITLE'] == "Stores REST API"
    assert app.config['API_VERSION'] == "v1"
    assert app.config['OPENAPI_VERSION'] == "3.0.3"
    assert app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] is False
    assert app.config['PROPAGATE_EXCEPTIONS'] is True

def test_blueprints_registered(app):
    """Test that blueprints are registered."""
    assert 'books' in app.blueprints

def test_home_page(client):
    """Test the home page."""
    response = client.get('/')
    assert response.status_code == 404  # Assuming no route is defined for home

# def test_create_app_with_docker_env(monkeypatch):
#     monkeypatch.setenv('DOCKER_CONTAINER', '1')
#     app = create_app()
#     assert app.config['SQLALCHEMY_DATABASE_URI'] == os.getenv('DATABASE_URL')

def test_create_app_without_docker_env(monkeypatch):
    monkeypatch.delenv('DOCKER_CONTAINER', raising=False)
    monkeypatch.setenv('DATABASE_URL_LOCAL', 'sqlite:///test.db')
    app = create_app()
    assert app.config['SQLALCHEMY_DATABASE_URI'] == 'sqlite:///test.db'