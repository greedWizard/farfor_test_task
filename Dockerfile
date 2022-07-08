FROM python:3.10.4-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

RUN apt-get update  && \
    apt install -y python3-dev \
    libboost-mpi-python-dev \
    gcc \
    musl-dev \
    libpq-dev postgresql postgresql-contrib \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip
RUN pip install poetry
ADD pyproject.toml .
RUN poetry install

COPY . .