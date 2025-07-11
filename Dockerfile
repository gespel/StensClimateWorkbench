FROM python:3
LABEL authors="Sten"

COPY . .

ENTRYPOINT ["python", "server.py"]