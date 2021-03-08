FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /recupera_credito_dj

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
