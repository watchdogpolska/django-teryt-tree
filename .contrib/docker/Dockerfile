# This is Dockerfile for development purposes only.
ARG PYTHON_VERSION='3.7'
FROM python:${PYTHON_VERSION}-slim
RUN mkdir /code /code/production
WORKDIR /code

# Install python dependencies
ENV PYTHONUNBUFFERED 1
RUN apt-get update \
&& apt-get install -y --no-install-recommends \
   default-libmysqlclient-dev \
   wait-for-it \
&& rm -rf /var/lib/apt/lists/*
COPY ./requirements*.txt ./
ARG DJANGO_VERSION='==2.2.*'
RUN pip install --no-cache-dir "django${DJANGO_VERSION}" -r requirements-test.txt
CMD ["bash", "-c", "python manage.py collectstatic --no-input && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]