import json
import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_response_success(client):
    response = client.get('/0')
    expected_response = {
        'extenso': 'zero'
    }
    assert json.loads(response.data) == expected_response


def test_response_error(client):
    response = client.get('/1000000')
    expected_response = {
        "message": "Number out of range"
    }
    assert json.loads(response.data) == expected_response
