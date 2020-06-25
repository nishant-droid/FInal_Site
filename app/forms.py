from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from app.models import User
from wtforms.fields.html5 import DateField, TimeField

class RegistrationForm(FlaskForm):
    username = StringField('Username',
                            validators=[DataRequired(), Length(min=5, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign up')
    def validate_username(self,username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken')
    
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('User already exist. Please login or choose forgot password')


class LoginForm(FlaskForm):
    #email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remeber me')
    submit = SubmitField('Login')
"""
    def validate_field(self,field):
        user = User.query.Filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username taken')
"""
class UploadForm(FlaskForm):
    hopper_date = DateField('Enter date of hopper file: ', validators=[DataRequired()], format= '%Y-%m-%d')
    hopper_time = TimeField('Enter time of hopper file: ', validators=[DataRequired()], format= '%H:%M')
    hopper_file = FileField(validators=[FileRequired()])
    submit = SubmitField('Upload file')