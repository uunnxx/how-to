# for python

# data.pickle
# database_exp.py
# Dockerfile
# requirements.txt

FROM python:latest

WORKDIR /src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY database_exp.py database_exp.py
COPY data.pickle data.pickle

CMD ["python", "-u", "database_exp.py"]


# for db
FROM postgres:latest

ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DATABASE=database
