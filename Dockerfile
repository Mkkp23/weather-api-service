FROM python:3.12-slim

WORKDIR /weather

COPY requirements.txt .

RUN ["pip","install","-r","requirements.txt"]

COPY . .

RUN ["python","manage.py","makemigrations"]
RUN ["python","manage.py","migrate"]

EXPOSE 8002

