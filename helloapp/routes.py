from flask import render_template
from helloapp import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Neil'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Neil Resume 2018', user=user, posts=posts)
    

@app.route('/test')
def test2():
    return "Hello, TEST!"