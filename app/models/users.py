from datetime import datetime
from app import db
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=True)
    gender = db.Column(db.Enum('M', 'F', 'O'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
