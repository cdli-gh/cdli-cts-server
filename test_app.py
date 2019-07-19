import pytest
import xml.dom.minidom

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
    rv = client.get(nemo, follow_redirects=True)
    text = rv.data.decode()
    assert 'Nemo' in text
    assert 'Text Collections' in text

    urn = 'urn:cts:cdli:test'
    page = 'default-collection-test-samples-converted-by-atf2cts'
    text = client.get(f'{nemo}/collections/{urn}/{page}').data.decode()
    assert 'CDLI Literary' in text


def cts_query(request, urn=None):
    '''Generate a nautilus query url for the given parameters.'''
    nautilus = main.nautilus.prefix
    url = f'{nautilus}/cts?request={request}'
    if urn:
        url += f'&urn={urn}'
    return url


def test_nautilus(client):
    '''Verify nautilus api service.'''
    rv = client.get(cts_query('GetCapabilities'))
    dom = xml.dom.minidom.parseString(rv.data)
    assert dom.documentElement.tagName == 'GetCapabilities'
    textgroups = dom.getElementsByTagName('textgroup')
    assert len(textgroups)
    urns = [element.getAttribute('urn') for element in textgroups]
    assert 'urn:cts:cdli:test' in urns

    works = dom.getElementsByTagName('work')
    urn = works[0].getAttribute('urn')
    rv = client.get(cts_query('GetPassage', urn))
    passage = xml.dom.minidom.parseString(rv.data)
    assert passage.documentElement.tagName == 'GetPassage'
    texts = passage.getElementsByTagName('text')
    assert len(texts) == 1
    bodies = texts[0].getElementsByTagName('body')
    assert len(bodies) == 1
    divs = bodies[0].getElementsByTagName('div')
    assert len(divs) > 0
    edition = divs[0]
    assert edition.getAttribute('type') == 'edition'
    assert edition.getAttribute('n').startswith(urn)
