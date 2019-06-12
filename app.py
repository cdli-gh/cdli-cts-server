'''Flask CTS webservice.

Serve the Canonical Text Services API for a collection of TEI xml files.
Following https://github.com/Capitains/tutorial-nemo
'''

from flask import Flask

flask_app = Flask("CTS webserver demo (nemo)")

if __name__ == '__main__':
    flask_app.run(debug=True)
