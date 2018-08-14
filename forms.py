from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(FlaskForm):
    first_name = StringField('First Name',validators=[DataRequired('Please enter first name')])
    last_name = StringField('Last Name',validators=[DataRequired('Please enter last name')])
    email = StringField('Email',validators=[DataRequired('Please enter your email'),Email()])
    password = PasswordField('Password',validators=[DataRequired('Please enter password'),Length(min=6,message="Must be at least 6 characters")])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')