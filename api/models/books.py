from ..db import db
from sqlalchemy.orm import relationship
from . import bookstore


class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    price = db.Column(db.Integer)
    image = db.Column(db.String(255))
    description = db.Column(db.String(1000))
   

    stores_relation = db.relationship('StoreModel', secondary='bookstore', backref=db.backref('books', lazy='dynamic'))
