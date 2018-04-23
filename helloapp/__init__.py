from flask import Flask
from helloapp.config import DebugConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(DebugConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'      # forces users to login first, login is the endpoint name for the login view

from helloapp import routes, models
