#!/bin/bash
docker run --rm --privileged multiarch/qemu-user-static --reset -p yes
docker buildx create --name mplat
docker buildx use mplat
docker buildx inspect --bootstrap
docker buildx build . --platform linux/amd64,linux/arm64 -t hiskyzen/autohcs:210727-2 -t hiskyzen/autohcs:latest --push