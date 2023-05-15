from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField, \
    RadioField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, ValidationError
from datetime import date


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email'), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)])
    remember = BooleanField('Remember me')


class SignupForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=80)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')


class ProfileForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(message='Invalid email'), Length(max=50)])
    date_of_birth = DateField('Date of Birth', format='%Y-%m-%d', validators=[Optional()])
    gender = RadioField('Gender', choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], validators=[Optional()])
    submit = SubmitField('Update Profile')

    def validate_date_of_birth(self, field):
        if field.data:
            if field.data and field.data > date.today():
                raise ValidationError('Date of birth cannot be in the future.')

    def validate_gender(self, field):
        if field.data not in ['M', 'F', 'O', None]:
            raise ValidationError('Not a valid gender value.')
