# see the base/ directory
FROM docker.io/fnndsc/pl-radial-distance-map:base-1

LABEL org.opencontainers.image.authors="FNNDSC <dev@babyMRI.org>" \
      org.opencontainers.image.title="pl-radial-distance-map" \
      org.opencontainers.image.description="Bi-directional mincchamfer"

WORKDIR /usr/local/src/pl-radial-distance-map

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
ARG extras_require=none
RUN pip install ".[${extras_require}]"

CMD ["bichamfer"]
