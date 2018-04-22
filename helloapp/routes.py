from helloapp import app
from helloapp.forms import LoginForm
from flask import render_template, flash, redirect, url_for


@app.route('/')
@app.route('/index')
def home_index():
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
    return render_template('index.html', title='Flask microblog', user=user, posts=posts)


@app.route('/test')
def test2():
    return "Hello, TEST!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format( form.username.data, form.remember_me.data))
        return redirect(url_for('home_index'))
    return render_template('login.html', title='Sign In', form=form)