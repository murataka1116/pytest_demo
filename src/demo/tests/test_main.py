import pytest
import testing_mod
import flask
from flask import Flask
from flask_mod import app
from flask_main import app1

def test_ok_sample():
    result = testing_mod.add_calc(1, 2)
    assert 3 == result


def test_flask_simple():
    app.config['TESTING'] = True
    client = app.test_client() 
    result = client.get('/')
    assert b'root' == result.data

def test_flask_simple1():
    app1.config['TESTING'] = True
    client = app1.test_client() 
    result = client.get('/')
    assert b'Hello World' == result.data

def test_flask_simple2():
    app1.config['TESTING'] = True
    client = app1.test_client() 
    result = client.get('/good')
    assert b'Good' == result.data
    
