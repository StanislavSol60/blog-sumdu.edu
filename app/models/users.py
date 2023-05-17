from datetime import datetime
from app import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from itsdangerous import URLSafeTimedSerializer, BadSignature, SignatureExpired
from flask import current_app


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.DateTime, nullable=True)
    gender = db.Column(db.Enum('M', 'F', 'O'), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    reset_token = db.Column(db.String(100), nullable=True)

    def set_password(self, new_password):
        self.password = generate_password_hash(new_password)

    def generate_reset_token(self):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        return serializer.dumps({'user_id': self.id}, salt='reset_token')

    @staticmethod
    def verify_reset_token(token):
        serializer = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        try:
            data = serializer.loads(token, salt='reset_token', max_age=1800)
            user_id = data['user_id']
            return User.query.get(user_id)
        except (BadSignature, SignatureExpired):
            return None
