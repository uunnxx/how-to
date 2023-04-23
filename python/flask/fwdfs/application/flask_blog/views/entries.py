# flask_blog/views/entries.py

from flask import request, redirect, url_for, render_template, flash, session
from flask_blog import app


@app.route('/')
def show_entries():
    return (
        render_template('entries/index.html')
        if session.get('logged_in')
        else redirect(url_for('login'))
    )
