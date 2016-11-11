from flask-wtf import Form
from wtforms import StringField, PasswordField, SubmitField

class signupForm(Form):
    first_name = StringField('first name')
    last_name = StringField('last name')
    email = StringField('Email')
    password = PasswordField('Password')
    submit = SubmitField('Sign up')