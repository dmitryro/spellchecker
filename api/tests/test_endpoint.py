from __future__ import absolute_import
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import app
import pytest

def test_route():
    assert False

def test_base_route():
    f_app = app.create_app()
    client = f_app.test_client()
    url = '/'
    response = client.get(url)
    assert response.get_data() == b'Spell checker Endpoint'
    assert response.status_code == 200


def test_get_route__success():
    assert False

def test_get_route__failure__bad_request():
    assert False
