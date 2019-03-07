from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.model import User

class Form(FlaskForm):
    username = StringField('Username', validators=[DataRequired(),])
    password = PasswordField("Password", validators=[DataRequired(),])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), ])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), ])
    password2 = PasswordField("Repeat Password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField('Register Now')

    def validate_name(self, username):
        user = User.query.filter_by(username=username.data).first()
        print("validate_name", user)
        if not user:
            raise ValidationError("You need a different name")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        print("validate_email", user)
        if user is not None:
            raise ValidationError("Email has been registered, try anotyher!!!")