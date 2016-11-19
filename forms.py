from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class signupForm(Form):
    first_name = StringField('first name', validators=[DataRequired("Please enter your first name")])
    last_name = StringField('last name', validators=[DataRequired("please enter your last name")])
    email = StringField('Email', validators=[DataRequired("Please enter your email"), Email("Please enter your email address")])
    password = PasswordField('Password', validators=[DataRequired("Please enter your password"), Length(min = 6, message="passwords must be six characters or more")])
    submit = SubmitField('Sign up')

class loginForm(Form):
    email = StringField('Email', validators=[DataRequired("Please enter your email"), Email("Please enter your email")])
    password = PasswordField('Password', validators =[DataRequired("Please enter your password")])
    submit = SubmitField("Sign in")

class AddressForm(Form):
    address = StringField('Address', validators=[DataRequired("please enter an address.")])
    submit = SubmitField('Search')