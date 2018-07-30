FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

RUN pip install --upgrade pip


WORKDIR /home/TODO_BE

COPY requirements.txt requirements.txt

RUN apt-get install -y gunicorn

RUN pip install -r requirements.txt

COPY core core
COPY dao dao
COPY helper helper
COPY app.py app.py
COPY config.py config.py
COPY boot.sh boot.sh
COPY gunicorn.conf.py gunicorn.conf.py
COPY wsgi.py wsgi.py


RUN chmod 777 boot.sh

ENV FLASK_APP app.py

RUN chown -R root:root ./
USER root

EXPOSE 5000
CMD ["flask", "db", "init"]
CMD ["flask", "db", "migrate"]
CMD ["flask", "db", "upgrade"]
CMD ["python", "helper/seed.py"]
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "app:app"]
