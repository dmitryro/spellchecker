from __future__ import absolute_import
import json
import os
import sys
import pytest
import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def test_base_route():
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/'
    response = client.get(url)
    data = json.loads(response.data)
    assert data['name'] == 'Spellchecker REST API Service'
    assert data['version'] == '1.0'
    assert response.status_code == 200


def test_get_route__success():
    """ Test case for word as is in dictionary """
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/spell/car'
    response = client.get(url)
    data = json.loads(response.get_data(as_text=True))
    assert data['correct'] == True
    assert len(data["suggestions"]) == 0
    assert response.status_code == 200


def test_get_route__success__missing_vowel():
    """ Test case for word wirh missing vowel """
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/spell/abndonmnt'
    response = client.get(url)
    data = json.loads(response.get_data(as_text=True))    
    assert data['correct'] == False    
    assert len(data["suggestions"]) > 0
    assert response.status_code == 200


def test_get_route__success__repeated():
    """ Test case for repeated latters """
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/spell/abandddon'
    response = client.get(url)
    data = json.loads(response.get_data(as_text=True))
    assert data['correct'] == False
    assert len(data["suggestions"]) > 0
    assert response.status_code == 200
    

def test_get_route__success__all_capital():
    """ Test case for all uppwer case  word """
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/spell/CAR'
    response = client.get(url)
    data = json.loads(response.get_data(as_text=True))
    assert data['correct'] == True
    assert len(data["suggestions"]) == 0
    assert response.status_code == 200


def test_get_route__success__capitalized():
    """ Test case for capitalized word """
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/spell/Car'
    response = client.get(url)
    data = json.loads(response.get_data(as_text=True))
    assert data['correct'] == True
    assert len(data["suggestions"]) == 0
    assert response.status_code == 200


def test_get_route__success__mixed():
    """ Test case for the word that was not found """
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/spell/bllllLLlln'
    response = client.get(url)
    data = json.loads(response.get_data(as_text=True))
    assert data['correct'] == False
    assert len(data["suggestions"]) > 0
    assert response.status_code == 200


def test_get_route__failure__not_found():
    """ Test case for the word that was not found """
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/spell/asymptomaticcase'
    response = client.get(url)
    data = json.loads(response.get_data(as_text=True))
    assert data['correct'] == False
    assert len(data["suggestions"]) == 0
    assert response.status_code == 404
