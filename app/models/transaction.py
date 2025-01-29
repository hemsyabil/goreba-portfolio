from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    portfolio_id = db.Column(db.Integer, db.ForeignKey('portfolio.id'))
    symbol = db.Column(db.String(10))
    transaction_type = db.Column(db.String(4))  # BUY/SELL
    quantity = db.Column(db.Float)
    price = db.Column(db.Float)
    date = db.Column(db.DateTime)
    currency = db.Column(db.String(3), default='USD')