FROM gcr.io/google_appengine/python:latest

WORKDIR /home/webapp

COPY ./requirements requirements

RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements/runtime_dependencies.txt

COPY ./webapp webapp
COPY ./app.py ./

ENV FLASK_APP app.py
CMD ["venv/bin/python", "app.py"]
