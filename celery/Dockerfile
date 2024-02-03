# Dockerfile

FROM cimg/python:3.12.1

WORKDIR /celery

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r ./requirements.txt

COPY . .
