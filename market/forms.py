from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.models import User


class RegisterForm(FlaskForm):

    def validate_username(self, check_username):
        user = User.query.filter_by(username=check_username.data).first()
        if user:
            raise ValidationError('User Name is already registered..! Please try a different User Name')

    def validate_email(self, check_email):
        email = User.query.filter_by(username=check_email.data).first()
        if email:
            raise ValidationError('Provided Email address is already registered..! Please try a different Email Address')

    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email Address:', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password:',  validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):

    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:',  validators=[DataRequired()])
    submit = SubmitField(label='Sign In')
