FROM ubuntu:16.04

# Update & upgrade apt-get
RUN apt-get update && apt-get upgrade -y

# Environment variables
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_APP=app/__init__.py
ENV APP_NAME="cloud_kitchen"

# Python install and packages
RUN apt-get install -y \
    tar \
    git \
    curl \
    nano \
	libpq-dev \
    python3.4 \
    python3-dev \
    python3-pip \
	postgresql-client \
    && apt-get autoremove \
    && apt-get clean

# Python 3.6 and pip3 as default
RUN easy_install3 pip && update-alternatives --install /usr/bin/python python /usr/bin/python3.4 1

# Install server stuff
RUN apt-get install -y  nginx \
    && pip install \
    virtualenv \
    gunicorn \
    flask

# Copy repo
COPY ./ /cloud_kitchen/
RUN mkdir /cloud_kitchen/logs

# Change workdir
WORKDIR /cloud_kitchen

# Install local dependencies
RUN virtualenv env && env/bin/pip install -r requirements.txt

# Map ports
EXPOSE 8000
EXPOSE 80

# Add Nginx configuration file
ADD cfn/nginx/conf.d/ /etc/nginx/conf.d
RUN rm -rf /etc/nginx/sites-available/default && rm -rf /etc/nginx/sites-enabled/default

ENTRYPOINT /bin/bash /cloud_kitchen/bin/run.sh