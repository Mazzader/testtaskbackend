FROM python:3.7

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

CMD ["gunicorn", "--chdir", "/app/rest", "--bind", ":8800", "--workers", "6", "rest.wsgi:application"]
