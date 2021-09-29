import pytest
import testing_mod
import flask_main
import flask
from flask import Flask
from flask_mod import app

def test_flask_simple():
    app.config['TESTING'] = True
    client = app.test_client() 
    result = client.get('/')
    assert b'root' == result.data