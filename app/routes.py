from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm, UploadForm
from flask_login import login_user, current_user, logout_user, login_required
from app.interface import Interface
from app.queries import Queries
from pathlib import Path
from app.balance_check import *

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
        print('after submit')
        user = request.form['username']
        passw = request.form['password']
        dbcur = interface.create_connection(user,passw)
        dbcur.execute('show databases')
        for db in dbcur:
            print(db)
        if interface.get_connection():
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Please check username and password.', 'danger')        
    return render_template('login.html', title='Login', form=form, condition= interface.get_connection())

@app.route('/logout')
def logout():
    interface.close_connection()
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

        