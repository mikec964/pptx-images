from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt()
login_manager = LoginManager(app)
login_manager.login_view = 'users.login' # class in routes.py
login_manager.login_message_category = 'info' # bootstrap css class
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_USER')
app.config['MAIL_PASSWORD'] = os.environ.get('EMAIL_PASS')
mail = Mail(app)

# from rpgtools import routes
from rpgtools.main.routes import main 
from rpgtools.posts.routes import posts
from rpgtools.users.routes import users

app.register_blueprint(main)
app.register_blueprint(posts)
app.register_blueprint(users)
