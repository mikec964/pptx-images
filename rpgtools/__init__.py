from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from rpgtools.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login' # class in routes.py
login_manager.login_message_category = 'info' # bootstrap css class

mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from rpgtools.errors.handlers import errors
    app.register_blueprint(errors)
    from rpgtools.main.routes import main 
    app.register_blueprint(main)
    from rpgtools.posts.routes import posts
    app.register_blueprint(posts)
    from rpgtools.users.routes import users
    app.register_blueprint(users)

    return app
