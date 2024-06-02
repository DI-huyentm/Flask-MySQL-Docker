from ..db import db
from sqlalchemy.orm import relationship


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255))

    books_relation = db.relationship('BookModel', secondary='bookstore', backref=db.backref('stores', lazy='dynamic'))
