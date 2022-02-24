FROM python:3.7-slim

ENV FLASK_APP=flask_app

RUN mkdir /app

COPY flask_app.py /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt 

EXPOSE 5017

CMD ["flask", "run", "--host", "0.0.0.0","--port", "5017"]
# RUN flask run --port 5017
