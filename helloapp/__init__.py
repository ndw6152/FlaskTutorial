from flask import Flask

from helloapp.config import DebugConfig

app = Flask(__name__)
app.config.from_object(DebugConfig)


from helloapp import routes
