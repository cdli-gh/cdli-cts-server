import pytest

import main


@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    yield main.app.test_client()


def test_index(client):
    '''Verify landing page.'''
    rv = client.get('/')
    assert 'CDLI Text Services' in rv.data.decode()


def test_nemo(client):
    '''Verify nemo pages.'''
    nemo = main.nemo.prefix
    print('Nemo prefix is', nemo)
    rv = client.get(nemo, follow_redirects=True)
    text = rv.data.decode()
    assert 'Nemo' in text
    assert 'Text Collections' in text

    urn = 'urn:cts:cdli:test'
    page = 'default-collection-atf2tei-test-examples'
    text = client.get(f'{nemo}/collections/{urn}/{page}').data.decode()
    assert 'belsunu' in text
