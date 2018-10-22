FROM python:2.7-slim
MAINTAINER Raphael Carloni Benzi <spawnbenzi@gmail.com>

ENV INSTALL_PATH /web_site
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "web_site.app:create_app()"
