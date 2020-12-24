FROM python:3.6-alpine

WORKDIR /home/webapp

COPY ./requirements.txt ./

RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY ./webapp webapp
COPY ./app.py ./

ENV FLASK_APP app.py
CMD ["venv/bin/python", "app.py"]