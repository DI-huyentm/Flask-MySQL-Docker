import pytest
from unittest.mock import MagicMock, patch
from api.app import create_app
from api.db import db
from api.models import BookModel

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    test_db_url = 'sqlite:///:memory:'
    
    app = create_app(test_db_url)
    app.config['TESTING'] = True

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

@pytest.fixture
def init_database(app):
    """Initialize the database with a sample book."""
    with app.app_context():
        book = BookModel(title="Sample Book", author="Author Name", price=100, image="sample.jpg", description="Sample Description")
        db.session.add(book)
        db.session.commit()
        yield db
        db.session.remove()

def test_get_all_books(client, init_database):
    response = client.get('/books/')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['title'] == "Sample Book"

def test_get_a_book(client, init_database):
    book = BookModel.query.first()
    response = client.get(f'/books/{book.id}/')
    assert response.status_code == 200
    assert response.json['title'] == "Sample Book"

def test_create_new_book(client):
    new_book = {
        "title": "New Book",
        "author": "New Author",
        "price": 150,
        "image": "new_image.jpg",
        "description": "New Description"
    }
    response = client.post('/books/', json=new_book)
    assert response.status_code == 201
    assert response.json['data']['book']['title'] == "New Book"

def test_create_new_book_validation_error(client):
    new_book = {
        "title": "New Book",
        "author": "New Author",
        "price": "invalid_price",
        "image": "new_image.jpg",
        "description": "New Description"
    }
    response = client.post('/books/', json=new_book)
    assert response.status_code == 400
    assert 'validation failed' in response.json['message']

def test_create_new_book_exception(client, monkeypatch):
    def mock_add(*args, **kwargs):
        raise Exception("Test Exception")
    monkeypatch.setattr('api.db.db.session.add', mock_add)
    new_book = {
        "title": "New Book",
        "author": "New Author",
        "price": 150,
        "image": "new_image.jpg",
        "description": "New Description"
    }
    response = client.post('/books/', json=new_book)
    assert response.status_code == 400
    assert 'Test Exception' in response.json['error']

def test_update_a_book(client, init_database):
    book = BookModel.query.first()
    updated_data = {
        "title": "Updated Book",
        "author": "Updated Author",
        "price": 200,
        "image": "updated_image.jpg",
        "description": "Updated Description"
    }
    response = client.put(f'/books/{book.id}/', json=updated_data)
    assert response.status_code == 200
    assert response.json['data']['book']['title'] == "Updated Book"

def test_update_a_book_validation_error(client, init_database):
    book = BookModel.query.first()
    updated_data = {
        "title": "Updated Book",
        "author": "Updated Author",
        "price": "invalid_price",
        "image": "updated_image.jpg",
        "description": "Updated Description"
    }
    response = client.put(f'/books/{book.id}/', json=updated_data)
    assert response.status_code == 400
    assert 'validation failed' in response.json['message']

def test_update_a_book_not_found(client):
    updated_data = {
        "title": "Updated Book",
        "author": "Updated Author",
        "price": 200,
        "image": "updated_image.jpg",
        "description": "Updated Description"
    }
    response = client.put('/books/999/', json=updated_data)
    assert response.status_code == 404
    assert response.json['message'] == "Book not found"



def test_delete_a_book(client, init_database):
    book = BookModel.query.first()
    response = client.delete(f'/books/{book.id}/')
    assert response.status_code == 200
    assert response.json['message'] == "Book deleted successfully"
    assert BookModel.query.get(book.id) is None

def test_delete_a_book_not_found(client):
    response = client.delete('/books/999/')
    assert response.status_code == 404
    assert response.json['message'] == "Book not found"

def test_delete_a_book_exception(client, init_database, monkeypatch):
    def mock_delete(*args, **kwargs):
        raise Exception("Test Exception")
    monkeypatch.setattr('api.db.db.session.delete', mock_delete)
    book = BookModel.query.first()
    response = client.delete(f'/books/{book.id}/')
    assert response.status_code == 400
    assert 'Test Exception' in response.json['error']


