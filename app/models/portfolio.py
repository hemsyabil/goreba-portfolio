from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    transactions = db.relationship('Transaction', backref='portfolio', lazy='dynamic')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
