# Python version can be changed, e.g.
# FROM python:3.8
# FROM docker.io/fnndsc/conda:python3.10.2-cuda11.6.0
FROM docker.io/python:3.11.0-slim-bullseye

LABEL org.opencontainers.image.authors="FNNDSC <Jennings.Zhang@childrens.harvard.edu>" \
      org.opencontainers.image.title="Radial Distance Map" \
      org.opencontainers.image.description="Bi-directional mincchamfer"

WORKDIR /usr/local/src/pl-radial-distance-map

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ARG extras_require=none
RUN pip install ".[${extras_require}]"

CMD ["bichamfer"]
