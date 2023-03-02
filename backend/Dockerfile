FROM python:3.10.9-buster

WORKDIR /app/backend


ENV VIRTUAL_ENV=/app/backend/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/Scripts:$PATH"


RUN apt-get update && apt-get install -y tesseract-ocr

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .