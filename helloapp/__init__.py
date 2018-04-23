from flask import Flask
from helloapp.config import DebugConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(DebugConfig)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from helloapp import routes, models
