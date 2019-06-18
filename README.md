# CDLI Text Services

[![Build Status (main branch)](https://travis-ci.org/cdli-gh/cdli-cts-server.svg?branch=master)](https://travis-ci.org/cdli-gh/cdli-cts-server)

This repo is a webservice which provides programmatic access to
texts from the [Cuneiform Digital Library Initiative](https://cdli.ucla.edu).

It loads a set of documents laid out according to
[Capitains Guidlines](http://capitains.org/pages/guidelines)
and makes them available over the
[Canonical Text Services](http://cite-architecture.org/cts/) api.

## Quickstart

```sh
pip install pipenv           # If you don't already have it.
git submodule update --init  # To download the corpus collection.
```

```sh
git submodule update
pipenv install --dev
pipenv run pytest
pipenv run python main.py
```

This starts a development server listening on the local machine.
It will automatically reload the server as changes to the source
are made.
From there you can
  [get available texts](http://localhost:5000/api/cts?request=GetCapabilities) or
  [fetch a text](http://localhost:5000/api/cts?request=GetPassage&urn=urn:cts:cdli:test.X001001).
There is also a [browse interface](http://localhost:5000/nemo/).

Additional text collections can be added under `corpora`.
The server must be manually restarted afterward.

## Deployment

The included `Dockerfile` can be used to deploy the server in a container.
