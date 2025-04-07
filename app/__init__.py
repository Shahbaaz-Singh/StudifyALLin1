from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['WTF_CSRF_ENABLED'] = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/database_name'
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = "admin_login"

migrate = Migrate(app, db)

@login_manager.user_loader
def load_user(user_id):
    if request.path.startswith('/admin/'):
        user = Admin.query.get(int(user_id))
    elif request.path.startswith('/employee/'):
        user = Employee.query.get(int(user_id))
    else:
        user = None
    return user

from .routes import *

def create_app():
    return app