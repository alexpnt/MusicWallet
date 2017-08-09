FROM python:2

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code

ADD requirements.txt /code/
RUN pip install -r /code/requirements.txt

COPY ./docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]