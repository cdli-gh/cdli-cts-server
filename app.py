'''Flask CTS webservice.

Serve the Canonical Text Services API for a collection of TEI xml files.
Following https://github.com/Capitains/tutorial-nemo
'''

import os

from flask import Flask
from flask_nemo import Nemo
from capitains_nautilus.cts.resolver import NautilusCTSResolver

flask_app = Flask("CTS webserver demo (nemo)")

corpora = [entry.path for entry in os.scandir('corpora') if entry.is_dir()]
print('app: resolver given', corpora)
resolver = NautilusCTSResolver(corpora)
resolver.parse()

nemo = Nemo(
        name='Nemo',
        app=flask_app,
        resolver=resolver,
        base_url=''
)

if __name__ == '__main__':
    flask_app.run(debug=True)
