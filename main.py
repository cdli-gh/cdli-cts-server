'''Flask CTS webservice.

Serve the Canonical Text Services API for a collection of TEI xml files.
Following https://github.com/Capitains/tutorial-nemo
'''

import os

from flask import Flask
from flask_nemo import Nemo
from capitains_nautilus.cts.resolver import NautilusCTSResolver
from capitains_nautilus.flask_ext import FlaskNautilus

app = Flask("CTS webserver demo (nemo)")

corpora = [entry.path for entry in os.scandir('corpora') if entry.is_dir()]
print('app: resolver given', corpora)
resolver = NautilusCTSResolver(corpora)
resolver.parse()

nautilus_api = FlaskNautilus(
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
def homepage():
    '''Placeholder home page to help visitors.

    We're mainly here to serve the nemo browser and api endoints,
    but provide a simple landing page in case we're serving the
    whole domain.'''
    return '''<!doctype html>
<html>
  <head>
    <meta charset=utf-8>
    <title>CDLI CTS webservice</title>
  </head>
  <body>
    <h1>CDLI Text Services</h1>
    <p>This server provide texts from the
       <a href=https://cdli.ucla.edu>Cuneiform Digital Library Initiative</a>.
    </p>
    <p>From here you can
    <ul>
      <li><a href=/nemo/>Browse the collection</a> with Nemo.</li>
      <li><a href=/api/cts?request=GetCapabilities>Query the CTS api</a>
          with Nautilus.</li>
    </ul>
    </p>
  </body>
</html>'''


if __name__ == '__main__':
    app.run(debug=True)
