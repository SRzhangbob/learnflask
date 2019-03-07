from app import app
from flask import render_template, flash, url_for, redirect
from app.form import Form

@app.route('/')
@app.route('/index')
def index():
    user = {"nickname": "boxer"}
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html", title= "Home", user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Form()
    if form.validate_on_submit():
        flash("Login requested for user {}, remember_me={}".format(
            form.username.data, form.remember_me.data))
        print("name, password:", form.username.data, form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)
