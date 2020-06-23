from flask import render_template, url_for, flash, redirect, request
from app import app, db, bcrypt
from app.models import User, Post
from app.forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required
from app.interface import Interface


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


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

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
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = request.form['username']
        passw = request.form['password']
        interface.create_connection(user,passw)
        if interface.get_connection():
            dbcur = interface.create_cursor()
            dbcur.execute('show databases')
            for dbs in dbcur:
                print (dbs)
            dbcur.close()
            next_page = request.args.get('next')
            if interface.get_connection:
                flash("Still get the connection", 'info')
            return redirect(next_page) if next_page else redirect(url_for('about'))
            
        else:
            flash('Please check username and password.', 'danger')
               
    return render_template('login.html', title='Login', form=form, check = interface.get_connection)

@app.route('/logout')
def logout():
    interface.close_connection()
    return redirect(url_for('home'))

@app.route('/account')
@login_required
def account():
    return render_template('account.html', title='Account')