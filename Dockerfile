FROM python:3.9
WORKDIR /usr/src/app

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE config.settings.prod

COPY . .