from helloapp import app, db
# from helloapp package import application named app
from helloapp.models import User, Post


@app.shell_context_processor
def make_shell_context():  # called when flask shell is run, starts a python interpreter with the following imports available
    return {'db': db, 'User': User, 'Post': Post}