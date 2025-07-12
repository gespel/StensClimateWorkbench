FROM python:3
LABEL authors="Sten"

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "server.py"]