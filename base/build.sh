#!/bin/bash -ex

exec docker buildx build --push \
    --platform linux/amd64,linux/arm64,linux/ppc64le \
    -t docker.io/fnndsc/pl-radial-distance-map:base-1 .
