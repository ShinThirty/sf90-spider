FROM gcr.io/google_appengine/python:latest

WORKDIR /home/webapp

COPY ./requirements.txt ./
COPY ./key.json ./

RUN python3 -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY ./webapp webapp
COPY ./app.py ./

ENV FLASK_APP app.py
ENV GOOGLE_APPLICATION_CREDENTIALS key.json
CMD ["venv/bin/python", "app.py"]