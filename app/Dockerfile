# pull official base image
FROM python:3.7.5

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --upgrade pip \
  && pip install -r requirements.txt

# copy project
COPY . /usr/src/app

# run gunicorn server - uncomment if we don't want to use docker-compose
# EXPOSE 8000
# CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app.api:app"]
