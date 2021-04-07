"""
FILE: app/routes.py

This file will contain decorators and their functions
"""

from flask import flash, jsonify, redirect, render_template, url_for, request
from flask_cors import CORS
from .__init__ import app, db
from .models import *
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.exceptions import BadRequest
from flask_jwt_extended import create_access_token


@app.route('/')
@app.route('/home')
def home():
    # TODO: Render homepage

    # Mock homepage below
    user = {'username': 'Sylvia'}

    return jsonify(user)
    


@app.route('/register', methods=['GET', 'POST'])
def register():
    # TODO: Render registration page
    # TODO: Implement OAuth
    """ Fair warning: Internal Server Error will occur if you try to submit a registration form """
    if current_user.is_authenticated:
        return redirect(url_for('account'))        # redirect logged-in users to their account page

    while True:
        try:
            register_json = request.get_json()      # if parsing fails, BadRequest exception is raised
        except BadRequest:
            register_json = request.get_json()
        else:
            new_username = register_json.get('username')
            new_password = register_json.get('password')

            while does_user_exist(new_username):
                return jsonify({'msg': 'Username already exists. Please choose a different one.'})

            if not does_user_exist(new_username):
                create_user(new_username, new_password)
                break
    
    return redirect(url_for('login'))



@app.route('/login', methods=['GET', 'POST'])
def login():
    # TODO: Render login page
    # TODO: Implement OAuth 
    if current_user.is_authenticated:
        return redirect(url_for('account'))
    
    while True:
        try:
            login_json = request.get_json()
        except BadRequest:
            login_json = request.get_json()
        else:
            username = login_json.get('username')
            password = login_json.get('password')

            if not verify_login(username, password):
                return jsonify({'msg': 'The username or password is incorrect. Please try again.'})
            
            elif verify_login(username, password):
                access_token = create_access_token(identity=username)
                this_user = get_user_obj(username)
                login_user(this_user)
                break
    
    return jsonify({'access_token': access_token})      # after the access token has been sent out, front end should redirect to '/account'



@app.route('/account', methods=['GET', 'POST'])
def account():
    pass


@app.route('/createProject', methods=['GET', 'POST'])
def createProject():
    pass


@app.route('/project', methods=['GET', 'POST'])
def project():
    pass


@app.route('/editProject', methods=['GET', 'POST'])
def editProject():
    pass


@app.route('/hardware', methods=['GET', 'POST'])
def hardware():
    pass


@app.route('/datasets', methods=['GET', 'POST'])
def datasets():
    pass





    

