from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='secret-key-goes-here',
        SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite',
        # SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)
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
        # db.drop_all()
        db.create_all()

    return app
