FROM python:3.9-alpine3.13

EXPOSE 8000

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY . .


RUN  python -m venv venv & \
    source venv/bin/activate & \
    pip3 install -r requirements.txt
