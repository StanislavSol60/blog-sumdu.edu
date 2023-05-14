from flask import Blueprint, render_template
from flask_login import current_user
# from . import db

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/profile')
def profile():
    if current_user.is_authenticated:
        return render_template('profile.html', name=current_user.name)
    else:
        return render_template('login.html')
