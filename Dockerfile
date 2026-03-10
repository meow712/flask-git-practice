FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y ca-certificates \
 && update-ca-certificates \
 && pip install --upgrade pip \
 && pip install flask

EXPOSE 5000

CMD ["python", "app.py"]
