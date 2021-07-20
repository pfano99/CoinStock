from flask_wtf import FlaskForm
from wtforms.validators import Email, EqualTo, Length, DataRequired, ValidationError
from wtforms import StringField, SelectField, PasswordField, SubmitField

from CoinStock.models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=16)])
    submit = SubmitField('login')

class SignupForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=16)])
    confirm_password = PasswordField('confirm Password', validators=[DataRequired(), Length(min=6, max=16), EqualTo('password')])
    submit = SubmitField('Search')

    def validate_email(self, email):
        user = User.query.filter_by(email=email)
        if user:
            raise ValidationError('That email is already taken, please try a different email')