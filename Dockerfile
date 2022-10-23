FROM python:3.9-slim

COPY . /app

WORKDIR /app

EXPOSE 8000

RUN pip3 install -r /app/requirements.txt
