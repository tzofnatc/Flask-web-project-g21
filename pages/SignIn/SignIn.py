from flask import Blueprint, render_template
from flask import Flask, redirect, url_for , render_template, request , session
from intract_with_DB import interact_db
import mysql.connector

# SignIn blueprint definition
SignIn = Blueprint('SignIn', __name__, static_folder='static', static_url_path='/SignIn', template_folder='templates')


# Routes
@SignIn.route('/SignIn', methods=[ 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        found = True
        if found:
            session['username'] = username
            session['user_password'] = password
            return render_template('SignIn.html')
        else:
            return render_template('SignIn.html')

@SignIn.route('/logout')
def logout_func():
    session['user_nickname'] = ''
    session['user_password'] = ''
    return render_template('SignIn.html')
