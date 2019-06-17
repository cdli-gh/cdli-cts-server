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
def homepage():
    '''Placeholder home page to help visitors.

    We're mainly here to serve the nemo browser and api endoints,
    but provide a simple landing page in case we're serving the
    whole domain.'''
    return f'''<!DOCTYPE html>
<html>
  <head>
    <meta charset=utf-8>
    <title>CDLI CTS webservice</title>
    <style>
      body {{
        width: 100%;
        margin: 0 auto;
        font-size: 14px;
        line-height: 20px;
      }}
      header {{
        background-color: lightgrey;
        padding: 20px;
      }}
      nav {{
        margin: 20px;
      }}
      h1, h2, h3 {{
        font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        line-height: 1;
      }}
      p {{
        font-family: "Palatino", "Palatino Linotype", "Georgia", "Serif";
      }}
    </style>
  </head>
  <body>
    <header>
    <h1>CDLI Text Services</h1>
    <p>This server provides programmatic access to texts from the
       <a href=https://cdli.ucla.edu>Cuneiform Digital Library Initiative</a>.
    </p>
    </header>
    <nav>
    <p>From here you can:
    <ul>
      <li><a href={nemo.prefix}/>Browse the collection</a> with Nemo.</li>
      <li><a href={nautilus.prefix}/cts?request=GetCapabilities>Query
          the CTS api</a> with Nautilus.</li>
    </ul>
    </p>
    <nav>
  </body>
</html>'''


if __name__ == '__main__':
    app.run(debug=True)
