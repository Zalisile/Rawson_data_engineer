FROM python:3.10

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY schema.sql ./
COPY schema.py ./

RUN chmod +x schema.py