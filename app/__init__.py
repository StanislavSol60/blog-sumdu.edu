from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv
import os

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()


def create_app(config_name='default'):
    load_dotenv('.flaskenv')

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_DATABASE_URI'),
        SQLALCHEMY_TRACK_MODIFICATIONS=os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS'),
        MAIL_SERVER=os.getenv('MAIL_SERVER'),
        MAIL_PORT=os.getenv('MAIL_PORT'),
        MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
        MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
        MAIL_USE_TLS=True,
        MAIL_USE_SSL=False
    )

    if config_name == 'testing':
        app.config.from_mapping(
            SQLALCHEMY_DATABASE_URI=os.getenv('SQLALCHEMY_TEST_DATABASE_URI'),
            SERVER_NAME=os.getenv('SERVER_NAME'),
            APPLICATION_ROOT=os.getenv('APPLICATION_ROOT'),
            TESTING=True,
            WTF_CSRF_ENABLED=False
        )

    db.init_app(app)
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'users.login'

    from app.models.users import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routers.users import users_bp
    app.register_blueprint(users_bp)

    from app.routers.posts import posts_bp
    app.register_blueprint(posts_bp)

    from app.routers.comments import comments_bp
    app.register_blueprint(comments_bp)

    with app.app_context():
        db.create_all()

    return app
