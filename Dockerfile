FROM docker.twistbioscience-staging.com/devops_slave_python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apt-get update && apt-get install -y \
    gsfonts \
    ncbi-blast+ \
    && curl -Os https://bin.equinox.io/c/ekMN3bCZFUn/forego-stable-linux-amd64.deb \
    && dpkg -i forego-stable-linux-amd64.deb \
    && rm forego-stable-linux-amd64.deb \
    && curl https://s3.us-east-2.amazonaws.com/twist-api-deps/wkhtmltopdf_linux-x86_64/wkhtmltopdf -o /usr/bin/wkhtmltopdf \
    && chmod 777 /usr/bin/wkhtmltopdf \
    && pip install numpy scipy

ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./sfconreset/ /code/
