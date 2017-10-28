#!/bin/bash -xe

docker rm -f hangman || true
docker run -d -i -t -v "$(pwd):/deploy/apps/hangman-game" -p 0.0.0.0:80:80 --name "hangman" "hangman:v.0.1" ./env/services.sh
