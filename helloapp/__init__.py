from flask import Flask
from configuration import DebugConfig

app = Flask(__name__)
app.config.from_object(DebugConfig)

from helloapp import routes