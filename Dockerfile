FROM python:3

WORKDIR /usr/src/app

RUN pip install aiogram

COPY bot.py /usr/src/app
