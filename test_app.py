import pytest

from main import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    yield app.test_client()


def test_index(client):
    '''Verify landing page.'''
    rv = client.get('/')
    print(rv.data)
    assert 'CDLI Text Services' in rv.data.decode()
