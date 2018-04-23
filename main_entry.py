from helloapp import app, db
# from helloapp package import application named app
from helloapp.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}