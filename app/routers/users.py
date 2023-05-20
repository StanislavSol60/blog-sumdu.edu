from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import current_user, login_user, logout_user, login_required
from app import db, mail
from app.forms.users import LoginForm, SignupForm, ProfileForm, ForgotPasswordForm, ResetPasswordForm
from app.models.users import User
from flask_mail import Message
import os

users_bp = Blueprint('users', __name__)
mail_sender = os.getenv('MAIL_SENDER')


@users_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.profile'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            return redirect(url_for('posts.my_posts'))
        flash('Invalid email or password')
    return render_template('login.html', form=form)


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
    return render_template('signup.html', form=form)


@users_bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users_bp.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            flash('The account associated with this email address was not found')
        else:
            token = user.generate_reset_token()
            user.reset_token = token
            db.session.commit()
            reset_link = url_for('users.reset_password', token=token, _external=True)
            msg = Message('Password Reset Request', sender=mail_sender, recipients=[user.email])
            msg.body = f"Hi {user.name},\n\nTo reset your password, click on the following link:\n{reset_link}\n\nIf you did not request a password reset, please ignore this email."
            mail.send(msg)
            flash('An email with instructions to reset your password has been sent.', 'info')
            return redirect(url_for('users.login'))
    return render_template('forgot_password.html', form=form)


@users_bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    user = User.verify_reset_token(token)
    if not user:
        flash('Invalid or expired token.', 'danger')
        return redirect(url_for('users.forgot_password'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        if form.password.data == form.confirm_password.data:
            user.set_password(form.password.data)
            db.session.commit()
            flash('Your password has been reset.', 'success')
            return redirect(url_for('users.login'))
        else:
            flash('Passwords do not match.', 'danger')
    return render_template('reset_password.html', form=form, token=token)


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

    # Pre-populate the form fields with the current user's information
    form.name.data = current_user.name
    form.email.data = current_user.email
    form.date_of_birth.data = current_user.date_of_birth
    form.gender.data = current_user.gender

    return render_template('profile.html', form=form)
