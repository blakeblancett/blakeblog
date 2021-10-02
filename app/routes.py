from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Blake'}
    posts = [
        {
            'author': {'username': 'Charlie'},
            'body': 'Beautiful day in Dayton!'
        },
        {
            'author': {'username': 'Claire'},
            'body': 'Ted Lasso is so good!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
