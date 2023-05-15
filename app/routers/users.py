from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from app import db
from app.forms.users import LoginForm, SignupForm, ProfileForm
from app.models.users import User

users_bp = Blueprint('users', __name__)


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('users.profile'))
        flash('Invalid email or password')
    return render_template('login.html', title='Sign In', form=form)


@users_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        # Check if user with email already exists
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash('Email already taken. Please choose another email.')
        else:
            # Create new user
            user = User(email=form.email.data, name=form.name.data, password=generate_password_hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            flash('Congratulations, you are now a registered user!')
            return redirect(url_for('users.login'))
    return render_template('signup.html', title='Register', form=form)


@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('posts.index'))


@users_bp.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.email = form.email.data
        current_user.date_of_birth = form.date_of_birth.data
        current_user.gender = form.gender.data

        db.session.commit()
        flash('Your profile has been updated!', 'success')
        return redirect(url_for('users.profile'))

    # Pre-populate the form fields with the current user's information
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.date_of_birth.data = current_user.date_of_birth
    form.gender.data = current_user.gender

    return render_template('profile.html', title='Edit Profile', form=form)
