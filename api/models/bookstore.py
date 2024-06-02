from ..db import db
from sqlalchemy.orm import relationship

class BookStoreModel(db.Model):
    __tablename__ = 'bookstore'

    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'), primary_key=True)
    quantity = db.Column(db.Integer, default=0)  # Additional metadata, if needed

    # Relationships
    book = db.relationship('BookModel', backref=db.backref('bookstores', cascade='all, delete-orphan'))
    store = db.relationship('StoreModel', backref=db.backref('bookstores', cascade='all, delete-orphan'))
