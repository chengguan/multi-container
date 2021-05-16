# syntax=docker/dockerfile:1
#FROM alpine:3.7
FROM ubuntu:20.04

WORKDIR /app
COPY requirements.txt requirements.txt
ADD . /app

RUN apt-get update \
  && apt-get install -y python3-pip \
  && pip3 install --no-cache-dir --upgrade pip \
  && pip3 install --no-cache-dir -r requirements.txt


#RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["uwsgi", "uwsgi.ini"]
#CMD [ "python", "./myflask.py" ]
