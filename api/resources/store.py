from flask import request, jsonify
from flask.views import MethodView

from ..db import db
from ..models import StoreModel, BookModel, BookStoreModel
from ..schemas import StoreSchema
from pydantic import ValidationError

# Create Flask Blueprint
from flask import Blueprint
stores = Blueprint("stores", __name__)

@stores.route('/', methods=['GET'])
def get_all_stores():
    # Retrieve all stores from the database
    all_stores = StoreModel.query.all()    
    stores_dict = []
    for store in all_stores:
        store_dict = {
            'id': store.id,
            'name': store.name,
            # Add other attributes as needed
        }
        stores_dict.append(store_dict)   
    return jsonify(stores_dict), 200

@stores.route('/<int:store_id>', methods=['GET'])
def get_a_store(store_id):
    store = StoreModel.query.get(store_id)
    if store is None:
        return jsonify(message="Store not found"), 404
    # Convert store data to a dictionary
    store_data = {
        'id': store.id,
        'name': store.name,
        # Add more attributes if needed
    }
    return jsonify(store_data), 200


@stores.route('/<int:store_id>/books', methods=['GET'])
def get_books_of_store(store_id):
    store = StoreModel.query.get(store_id)
    if store is None:
        return jsonify(message="Store not found"), 404    
   
    books_with_quantity = []
    
    # Retrieve all books associated with the store
    books = store.books
    # Serialize the book objects into a list of dictionaries
    serialized_books = []
    for book in books:
        book_quantity = BookStoreModel.query.filter_by(book_id=book.id, store_id=store_id).first()
        quantity = book_quantity.quantity if book_quantity else 0

        serialized_book = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'price': book.price,
            'image': book.image,
            'description': book.description,
            'quantity': quantity
        }
        books_with_quantity.append(serialized_book)
    
    return jsonify(books_with_quantity), 200


@stores.route('/', methods=['POST'])
def create_new_store():
    try:
        # Validate request data using Pydantic
        data = request.json
        store_data = StoreSchema(**data) 
        
        # Create the store
        store = StoreModel(
            name=store_data.name
        )
        db.session.add(store)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'data': {
                'store': {
                    'id': store.id,
                    'name': store.name
                }
            }
        }), 201
    except ValidationError as e:
        return jsonify({
            'status': 'fail',
            'message': 'validation failed',
            'error': str(e)
        }), 400
    except Exception as e:
        return jsonify({
            'status': 'fail',
            'error': str(e)
        }), 400
