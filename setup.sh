#!/bin/bash -xe

image=$1
version=$2

docker build -t "$image:$version" .
