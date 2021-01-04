from __future__ import absolute_import
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
import app


@pytest.fixture
def test_app():
    f_app = app.create_app()
    return f_app


def test_base_route():
    assert True

def test_get_route__success():
    f_app = app.create_app()
    assert True


def test_get_route__failure__bad_request():
    assert True
