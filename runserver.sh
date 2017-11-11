#!/bin/bash -xe

argc=$#
argv=($@)

Runserver(){
	Remove;
	docker run $opt "$(pwd):$workdir" -p $port --name "$image" "$image:$img_version" $services $server $ini;
}

Remove(){
	docker rm -f $image || true;
}

Option(){
	for ((i = 7; i <= $(( $argc - 1 )); i++)); do
	    opt=$opt" "${argv[i]}
	done
}

server=$1
ini=$2
image=$3
img_version=$4
workdir=$5
port=$6
services=$7
Option

Runserver

if [ $server == uwsgi ] && [ $ini == local ]; then
	tail -f uwsgi.log
elif [ $server == gunicorn ] && [ $ini == local ]; then
	tail -f gunicorn.log
fi
