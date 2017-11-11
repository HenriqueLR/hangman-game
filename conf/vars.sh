#!/bin/bash

export CONF="$(pwd)/$(find . -name "*.ini"|cut -d"/" -f2)"
env | grep '^CONF='
