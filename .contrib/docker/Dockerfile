# This is Dockerfile for development purposes only.
ARG PYTHON_VERSION='3.10'
FROM python:${PYTHON_VERSION}
RUN mkdir /code /code/production
WORKDIR /code

# Install python dependencies
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
&& apt-get install -y --no-install-recommends \
   wait-for-it \
&& rm -rf /var/lib/apt/lists/*
COPY ./requirements*.txt ./
ARG DJANGO_VERSION='==4.2.*'
RUN bash -c "if [[ "${DJANGO_VERSION}" == 'master' ]]; then \
pip install --no-cache-dir -r requirements-test.txt https://github.com/django/django/archive/master.tar.gz; else \
pip install --no-cache-dir -r requirements-test.txt \"django${DJANGO_VERSION}\"; fi"
CMD python manage.py runserver 0.0.0.0:8000
