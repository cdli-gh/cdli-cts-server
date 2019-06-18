#!/bin/bash -e

NAME=cdli-cts-server
IMAGE=${NAME}
NET="127.0.0.1:5048"

# Build an updated container image.
docker build -t ${IMAGE} .

# Remove the old container, if any.
if [ -n "$(docker ps --quiet --all --filter name=${NAME})" ]; then
    docker stop ${NAME}
    docker rm ${NAME}
fi

# Start the new container.
docker run -d -p ${NET}:80/tcp --name ${NAME} ${IMAGE}

echo "Container ${NAME} bound to ${NET}."
