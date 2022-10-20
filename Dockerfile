FROM python:3.9

COPY . /fapp

WORKDIR /fapp

EXPOSE 8000

RUN pip3 install -r /app/requirements.txt
