FROM python:latest

RUN mkdir /app
WORKDIR /app

ADD . /app/

RUN pip install -r requirements.txt

EXPOSE 8888

RUN python manage.py migrate
CMD ["uwsgi", "--ini", "uwsgi.ini"]



