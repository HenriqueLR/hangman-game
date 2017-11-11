#!/bin/bash -xe

server=$1
ini=$2

sudo cp ./env/nginx/default /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

if [ $server = uwsgi ]; then
	sudo uwsgi --ini /deploy/apps/hangman-game/env/res/$ini.ini --logto uwsgi.log
elif [ $server = gunicorn ]; then
	sudo cp ./env/supervisord/supervisord.conf /etc/supervisord.conf
	sudo supervisord -c /etc/supervisord.conf
	sudo supervisorctl restart all
	/bin/bash
fi
