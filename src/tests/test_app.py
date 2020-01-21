import json
import pytest

from app import app


@pytest.fixture
def client():
    return app.test_client()


def test_response_ok(client):
    response = client.get('/')
    expected_response = {
        'input': 'not implemented',
        'output': 'not implemented'
    }
    assert json.loads(response.data) == expected_response
