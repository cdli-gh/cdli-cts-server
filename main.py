'''Flask CTS webservice.

Serve the Canonical Text Services API for a collection of TEI xml files.
Following https://github.com/Capitains/tutorial-nemo
'''

import os
import requests

import flask
from flask_nemo import Nemo
from capitains_nautilus.cts.resolver import NautilusCTSResolver
from capitains_nautilus.flask_ext import FlaskNautilus

app = flask.Flask("CTS webserver demo (nemo)")

corpora = [entry.path for entry in os.scandir('corpora') if entry.is_dir()]
print('app: resolver given', corpora)
resolver = NautilusCTSResolver(corpora)
resolver.parse()

nautilus = FlaskNautilus(
        prefix='/api',
        app=app,
        resolver=resolver
)

nemo = Nemo(
        name='Nemo',
        app=app,
        resolver=resolver,
        base_url='/nemo'
)


@app.route('/')
def home():
    '''Placeholder home page to help visitors.

    We're mainly here to serve the nemo browser and api endoints,
    but provide a simple landing page in case we're serving the
    whole domain.'''
    return flask.render_template('index.html',
                                 nemo=nemo.prefix,
                                 nautilus=nautilus.prefix,
                                 requests=requests)


if __name__ == '__main__':
    app.run(debug=True)
