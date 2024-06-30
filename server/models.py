from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy_serializer import SerializerMixin


metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(200), nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'), nullable=False)

    customer = db.relationship('Customer', backref='reviews')
    item = db.relationship('Item', backref='reviews')

    def __repr__(self):
        return f'<Review {self.id}>'
    
class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f'<Customer {self.id}, {self.name}>'


class Item(db.Model):
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Item {self.id}, {self.name}, {self.price}>'

