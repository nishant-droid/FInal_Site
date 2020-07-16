
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager




# from urllib.parse import quote_plus as urlquote

app = Flask(__name__)
app.config['SECRET_KEY'] = '5cbad136ea703b724fc08b5e0301c042830757eb'
# app.config['SQLALCHEMY_DATABSE_URI'] = 'mysql://root:%s@localhost:3306/posts'
#  %urlquote('Password@123')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view='login'
login_manager.login_message_category = 'info'


from app import routes