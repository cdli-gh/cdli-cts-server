FROM tiangolo/meinheld-gunicorn-flask

# pipenv can't find unicorn, so duplicate dependencies here.
RUN pip install flask-nemo capitains_nautilus requests

# Copy app files last for faster rebuilds.
COPY . /app

