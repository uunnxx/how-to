# ../flask_blog/views.py

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


# @app.route(URL)
# def function():
#     pass

@app.route('/')
def show_entries():
    return (
        render_template('entries/index.html')
        if session.get('logged_in')
        else redirect(url_for('login'))
    )


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            flash('User name is different!')
        elif request.form['password'] != app.config['PASSWORD']:
            flash('Password is different')
        else:
            session['logged_in'] = True
            flash('Login successful')
            return redirect(url_for('show_entries'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('Logged Out')
    return redirect(url_for('show_entries'))
