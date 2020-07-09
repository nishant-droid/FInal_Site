from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm, UploadForm, MasterBranchForm, MasterCITForm, MasterBankForm, MasterMFTForm
from flask_login import login_user, current_user, logout_user, login_required
from app.interface import Interface
from app.queries import Queries
from pathlib import Path
from app.mysqlconnection import errorcode

posts = [
    
    {
        'author':'LeDoux Karia',
        'title': 'Blog Post 1',
        'content': 'This is the first post',
        'date_posted': 'December 15 2020'
    },
    {
        'author':'Nisant Patel',
        'title': 'Blog Post 2',
        'content': 'This is the second post',
        'date_posted': 'April 27 2020'
    },
    {
        'author':'Nishith Acharya',
        'title': 'Blog Post 3',
        'content': 'This is the third post',
        'date_posted': 'May 26 2020'
    }

]

interface = Interface()
query = Queries()


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts, condition=interface.get_connection())

@app.route('/about')
def about():
    return render_template('about.html', title='About', condition= interface.get_connection())

@app.route('/register', methods=['POST','GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created! You are now able to login!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = request.form['username']
        passw = request.form['password']
        dbcur = interface.create_connection(user,passw)
        if interface.get_connection():
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Please check username and password.', 'danger')         
    return render_template('login.html', title='Login', form=form, condition= interface.get_connection())

@app.route('/logout')
def logout():
    if interface.get_connection():
        interface.close_connection()
        if interface.get_connection():
            print("Get the actual connection even after disconnecting")
        else:
            print("Doesnt Get the connection after disconnecting when get_connection is called")
        return redirect(url_for('home'))

@app.route('/account')
def account():
    if interface.get_connection():
        return render_template('account.html', title='Account', condition= interface.get_connection())
    else:
        flash('Please login', 'info')
        return redirect(url_for('login'))

@app.route('/hopper', methods=['GET','POST'])
def hopper():
    if interface.get_connection():
        form=UploadForm()
        if form.validate_on_submit():
            hopper_date = request.form['hopper_date']
            hopper_time = request.form['hopper_time']
            if form.hopper_file.data:
                hfile = form.hopper_file.data
                file_path = interface.check_file(hfile)
                if file_path:
                    interface.file_manupilation(file_path,hopper_date,hopper_time)
                    dbcur = interface.create_cursor()
                    dbcur.execute(query.db_selection())
                    dbcur.execute(query.push_file())
                    interface.commit_DB()
                    flash('File uploaded successfully.', 'success')
                else:
                    flash('File not supported. Please check the file.', 'danger')
    else:
        flash('Please login to continue.', 'info')
        return redirect(url_for('login'))
    return render_template('hopper.html', title='Upload Hopper File', form=form, condition= interface.get_connection())

@app.route("/post/new", methods=["GET","POST"])
def new_post():
    return render_template('create_post.html', title='New Post', form=form, condition= interface.get_connection())

@app.route("/monthlyPlanner", methods=['GET','POST'])
def monthlyPlanner():
    column_list = ["Station ID","Total Cash","Hopper File Date","Hopper File Time"]

    return render_template('monthlyPlanner.html', title='Monthly Visit Planner', columns= column_list, items=temp)

@app.route("/masterBranch", methods=["GET","POST"])
def branchmaster():
    form = MasterBranchForm()
    if interface.get_connection():
        if form.validate_on_submit():
            branchcode = request.form['branch_code']
            branchname = request.form['branch_name']
            atmcode = request.form['atm_code']
            bankcode = request.form['bank_code']
            bankadd = request.form['bank_add']
            email = request.form['email']
            emailgroup = request.form['email_group']
            dbcur = interface.create_cursor()
            try:
                dbcur.execute(query.add_data_branch(branchcde,branchname,atmcode,bankcode,bankadd,email,emailgroup))
                interface.commit_DB()
                flash('Data added!', 'success')
            except:
                flash(f'Something went Wrong!!', 'danger')

    else:
        flash('Please login to continue.', 'info')
        return redirect(url_for('login'))
    return render_template('masterBranch.html', title='Branch Data',form = form, condition = interface.get_connection() )

@app.route("/masterCIT", methods=["GET","POST"])
def citmaster():
    form = MasterCITForm()
    if interface.get_connection():
        if form.validate_on_submit():
            citcode = request.form['cit_code']
            citname = request.form['cit_name']
            bankaccdetails = request.form['bank_account_details']
            add = request.form['address']
            contactpersonname = request.form['contact_person_name']
            contactpersonnumber = request.form['contact_person_mobile_number']
            contactpersonemail = request.form['contact_person_email']
            dbcur = interface.create_cursor()
            try:
                dbcur.execute(query.add_data_CIT(citcode,citname,bankaccdetails,add,contactpersonname,contactpersonnumber,contactpersonemail))
                interface.commit_DB()
                flash('Data added!', 'success')
            except:
                flash(f'Something went Wrong!!', 'danger')

    else:
        flash('Please login to continue.', 'info')
        return redirect(url_for('login'))
    return render_template('masterCIT.html', title='CIT Data',form = form, condition = interface.get_connection() )


@app.route("/masterBank", methods=["GET","POST"])
def bankmaster():
    form = MasterBankForm()
    if interface.get_connection():
        if form.validate_on_submit():
            bankcode = request.form['bank_code']
            bankname = request.form['bank_name']
            bankaccdetails = request.form['bank_account_details']
            add = request.form['address']
            miscellaneous  = request.form['miscellaneous']
            dbcur = interface.create_cursor()
            try:
                dbcur.execute(query.add_data_Bank(bankcode,bankname,bankaccdetails,add,miscellaneous))
                interface.commit_DB()
                flash('Data added!', 'success')
            except:
                flash(f'Something went Wrong!!', 'danger')

    else:
        flash('Please login to continue.', 'info')
        return redirect(url_for('login'))
    return render_template('masterBank.html', title='Bank Data',form = form, condition = interface.get_connection() )

@app.route("/masterMFT", methods=["GET","POST"])
def mftmaster():
    form = MasterMFTForm()
    if interface.get_connection():
        if form.validate_on_submit():
            mftid = request.form['mft_id']
            sitename = request.form['site_name']
            district = request.form['district']
            bankcode = request.form['bank_code']
            branchcode = request.form['branch_code']
            citname = request.form['cit_name']
            citcode = request.form['cit_code']
            cassetteconfig = request.form['cassette_configuration']
            cashlivedate = request.form['cash_live_date']
            techlivedate = request.form['tech_live_date']
            ubscode = request.form['ubs_code']
            routenumber = request.form['route_number']
            sequencenumber = request.form['sequence_number']
            atmserialnumber = request.form['atm_serial_number']
            secretaryname = request.form['secretary_name']
            secretarynumber = request.form['secretary_number']
            engineername = request.form['engineer_name']
            engineernumber = request.form['engineer_number']
            cashremovaldate = request.form['cash_removal_date']
            cashremovalreason = request.form['cash_removal_reason']
            closuretype = request.form['closure_type']
            closuredate = request.form['closure_date']
            closureremark = request.form['closure_remark']
            salarypaymentdate = request.form['salary_payment_date']
            salaryperpayment = request.form['salary_per_payment']
            dbcur = interface.create_cursor()
            try:
                dbcur.execute(query.add_data_MFT( mftif, sitename, district, bankcode, branchcode, citname, citcode, cassetteconfig, cashlivedate,techlivedate, ubscode, routenumber, sequencenumber, atmserialnumber,secretaryname, secretarynumber, engineername, engineernumber, cashremovaldate, cashremovalreason, closuretype, closuredate, closureremark, salarypaymentdate, salaryperpayment))
                interface.commit_DB()
                flash('Data added!', 'success')
            except:
                flash(f'Something went Wrong!!', 'danger')

    else:
        flash('Please login to continue.', 'info')
        return redirect(url_for('login'))
    return render_template('masterMFT.html', title='Bank Data',form = form, condition = interface.get_connection() )