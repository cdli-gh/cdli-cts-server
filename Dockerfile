FROM tiangolo/meinheld-gunicorn-flask

# pipenv can't find unicorn, so duplicate dependencies here.
RUN pip install flask-nemo capitains_nautilus

# Copy app files last for faster rebuilds.
COPY . /app

