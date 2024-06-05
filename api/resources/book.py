from flask import request, jsonify
from flask.views import MethodView
# from flask_smorest import Blueprint, abort
# from sqlalchemy.exc import SQLAlchemyError

from ..db import db
from ..models import BookModel
from ..schemas import BookSchema, BookUpdateSchema
from pydantic import ValidationError


# Create Flask Blueprint
from flask import Blueprint
books = Blueprint("books", __name__)

@books.route('/', methods=['GET'])
def get_all_books():
    # Retrieve all books from the database
    all_books = BookModel.query.all()
    books_dict = []
    for book in all_books:
        book_dict = {
            'id': book.id,
            'title': book.title,
            'author': book.author,
            'price': book.price,
            'image': book.image,
            'description': book.description
        }
        books_dict.append(book_dict)   
    return jsonify(books_dict), 200

@books.route('/<int:book_id>', methods=['GET'])
def get_a_book(book_id):
    book = BookModel.query.get(book_id)
    if book is None:
        return jsonify(message="Book not found"), 404
    return jsonify({
        'id': book.id,
        'title': book.title,
        'author': book.author,
        'price': book.price,
        'image': book.image,
        'description': book.description
    })


@books.route('/', methods=['POST'])
def create_new_book():
    try:
        data=request.json
        book_data = BookSchema(**data)
        book = BookModel(
            title= book_data.title,
            author= book_data.author,
            price= book_data.price,
            image= book_data.image,
            description= book_data.description
        )
        db.session.add(book)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'data': {
                'book': {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'price': book.price,
                    'image': book.image,
                    'description': book.description,
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


@books.route('/<int:book_id>', methods=['PUT'])
def update_a_book(book_id):
    try:
        data = request.json
        # Validate request data using BookUpdateSchema
        book_data = BookUpdateSchema(**data)

        # Retrieve the book from the database
        book = BookModel.query.get(book_id)
        if book is None:
            return jsonify(message="Book not found"), 404

        # Update the book attributes if provided in the request
        if book_data.title:
            book.title = book_data.title
        if book_data.author:
            book.author = book_data.author
        if book_data.price:
            book.price = book_data.price
        if book_data.image:
            book.image = book_data.image
        if book_data.description:
            book.description = book_data.description

        # Commit the changes to the database
        db.session.commit()

        # Return the updated book information
        return jsonify({
            'status': 'success',
            'data': {
                'book': {
                    'id': book.id,
                    'title': book.title,
                    'author': book.author,
                    'price': book.price,
                    'image': book.image,
                    'description': book.description
                }
            }
        }), 200
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

@books.route('/<int:book_id>', methods=['DELETE'])  
def delete_a_book(book_id):
    try:
        book = BookModel.query.get(book_id)
        if book is None:
            return jsonify(message="Book not found"), 404
        db.session.delete(book)
        db.session.commit()

        return jsonify({
            'status': 'success',
            'message': 'Book deleted successfully'
        }), 200
    
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
