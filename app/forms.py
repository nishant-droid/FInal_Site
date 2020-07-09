from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, TextAreaField
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

class MasterBranchForm(FlaskForm):
    branch_code = StringField('Branch Code', validators=[Length(max=20), DataRequired()])
    branch_name = StringField('Branch Name', validators=[Length(max=50), DataRequired()])
    atm_code = StringField('ATM Code', validators=[DataRequired(), Length(max=20)])
    bank_code = StringField('Bank Code', validators=[DataRequired(), Length(max=20)])
    bank_add = TextAreaField('Bank Address', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    email_group = IntegerField('Email Group', validators=[DataRequired()])
    submit = SubmitField('Add Data')

class MasterCITForm(FlaskForm):
    cit_code = StringField('CIT Code', validators=[Length(max=20), DataRequired()])
    cit_name = StringField('CIT Name', validators=[Length(max=50), DataRequired()])
    bank_account_details = StringField('Bank Account Details', validators=[DataRequired(), Length(max=20)])
    address = TextAreaField('Address', validators=[DataRequired()])
    contact_person_name = StringField('Contact Person Name', validators=[DataRequired(), Length(max=20)])
    contact_person_mobile_number = IntegerField('Email', validators=[DataRequired()])
    contact_person_email = StringField('Email Group', validators=[DataRequired(), Email()])
    submit = SubmitField('Add Data')

class MasterBankForm(FlaskForm):
    bank_code = StringField('Bank Code', validators=[Length(max=20), DataRequired()])
    bank_name = StringField('Bank Name', validators=[Length(max=50), DataRequired()])
    bank_account_details = StringField('Bank Account Details', validators=[DataRequired(), Length(max=20)])
    address = TextAreaField('Address', validators=[DataRequired()])
    miscellaneous = TextAreaField('Comments')
    submit = SubmitField('Add Data')

class MasterMFTForm(FlaskForm):
    mft_id = StringField('MFT ID', validators=[DataRequired(), Length(max=20)])
    site_name = StringField('Site Name', validators=[DataRequired(), Length(max=25)])
    district = StringField('District', validators=[DataRequired(), Length(max=20)])
    bank_code = IntegerField('Bank Code', validators=[DataRequired()])
    branch_code = IntegerField('Branch Code', validators=[DataRequired()])
    cit_name = StringField('CIT Name', validators=[DataRequired(), Length(max=20)])
    cit_code = StringField('CIT Code', validators=[DataRequired(), Length(max=20)])
    cassette_configuration = StringField("Cassette Configuration", validators=[DataRequired(), Length(max=5)])
    cash_live_date = DateField('Cash Live Date', validators=[DataRequired()])
    tech_live_date = DateField('Tech Live Date', validators=[DataRequired()])
    ubs_code = StringField('UBS Code', validators=[DataRequired(), Length(max=20)])
    route_number = StringField('Route Number', validators=[DataRequired(), Length(max=5)])
    sequence_number = StringField('Sequence Number', validators=[DataRequired(), Length(max=20)])
    atm_serial_number = IntegerField('ATM Serial Number', validators=[DataRequired()])
    secretary_name = StringField('Secretary Name', validators=[DataRequired(), Length(max=20)])
    secretary_number = IntegerField('Secretary Number', validators=[DataRequired()])
    engineer_name = StringField('Engineer Name', validators=[DataRequired(), Length(max=20)])
    engineer_number = IntegerField('Engineer Number', validators=[DataRequired()])
    cash_removal_date = DateField('Cash Removal Date') #check if it required or not
    cash_removal_reason = StringField('Cash Removal Reason', validators=[Length(max=20)])
    closure_type = StringField('Closure Type', validators=[Length(max=10)])
    closure_date = DateField('Closure Date')#check of if the data is required
    closure_remark = TextAreaField('Closure Remarks')#check of if the data is required
    salary_payment_date = DateField('Salary Payment Date', validators=[DataRequired()])
    salary_per_payment = IntegerField('Estimate Salary per Payment', validators=[DataRequired()])
    submit = SubmitField('Add Data')