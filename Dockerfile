FROM python:3.7-slim

ENV FLASK_APP=flask_app

RUN mkdir /app
COPY tween_m.pkl /app
COPY flask_app.py /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt && python -m pip install --upgrade pip

EXPOSE 5017

CMD ["flask", "run", "--host", "0.0.0.0","--port", "5017"]
# RUN flask run --port 5017

