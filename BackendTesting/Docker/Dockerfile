FROM python:3

RUN nvm install 12.16.1
RUN nvm use 12.16.1

ENV PYTHONBUFFERED 1

RUN pip install pip-tools
RUN pip-compile requirements.in

RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt
COPY . /code/