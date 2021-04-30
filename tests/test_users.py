
"""Tests for the users functionality of the API
This includes registration and login
"""
from api import app as myApp
from tests import simplicity_test
# from tests import test
import json
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, verify_jwt_in_request



# @test("Hello world test")
@simplicity_test
def test_hello_world(client, request):
    res = client.get('/api')
    # print(res)
    assert b"Simplicity API" in res.data

@simplicity_test
def test_register_new_user(client, request):
    user_data = {
        "username": "test_new_user",
        "email": "test@mail.com",
        "password": "test"
    }
    res = client.post('/api/register', json=user_data)
    assert res.status_code == 200
    assert b"token" in res.data

@simplicity_test
def test_register_user_email_exists(client, request):
    user_data = {
        "username": "test_new_user_2",
        "email": "test@mail.com",
        "password": "test"
    }
    res = client.post('/api/register', json=user_data)
    assert res.status_code == 409
    assert b"Email already exists" in res.data

@simplicity_test
def test_register_user_username_exists(client, request):
    user_data = {
        "username": "test_new_user",
        "email": "test@mail2.com",
        "password": "test"
    }
    res = client.post('/api/register', json=user_data)
    assert res.status_code == 409
    assert b"Username already exists" in res.data

@simplicity_test
def test_login_godmin_user(client, request):
    user_data = {
        "username": "admin",
        "email": "admin@admin",
        "password": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
    }
    res = client.post('/api/login', json=user_data)
    assert res.status_code == 200
    assert b"token" in res.data

#TODO: Bad Logins

@simplicity_test
def test_get_user(client, requests):
    user_data = {
        "username": "admin",
        "email": "admin@admin",
        "password": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
    }
    access_token = create_access_token(identity=user_data.get("username"))
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    res = client.get('/api/user', headers=headers, query_string={"username": user_data.get("username")})
    assert res.status_code == 200
    print(res)

#TODO: Bad Get Users

@simplicity_test
def test_get_num_users(client, requests):
    user_data = {
        "username": "admin",
        "email": "admin@admin",
        "password": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"
    }
    access_token = create_access_token(identity=user_data.get("username"))
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    res = client.post('/api/getNumUsers', headers=headers)
    assert res.status_code == 200
    print(res.data)

##TODO: Bad Get Number Users

@simplicity_test
def test_update_user(client, requests):
    user_data = {
        "username": "admin",
        "email": "admin@admin",
        "curPassword": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08", #test
        "is_admin": True,
        "password": "60303ae22b998861bce3b28f33eec1be758a213c86c93c076dbe9f558c11c752"
    }
    access_token = create_access_token(identity=user_data.get("username"))
    headers = {
        'Authorization': 'Bearer {}'.format(access_token)
    }
    res = client.post('/api/update_user', headers=headers, json=user_data)
    print(res.data)
    assert res.status_code == 200

#TODO: Bad update users
    

# def test_new_user_as_admin(client):

