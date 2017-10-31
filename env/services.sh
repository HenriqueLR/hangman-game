#!/bin/bash -xe

sudo /etc/init.d/nginx restart

if [ "$1" = "uwsgi" ]; then
	sudo uwsgi --ini /deploy/apps/hangman-game/env/res/local.ini --logto uwsgi.log
elif [ "$1" = "gunicorn" ]; then
	sudo supervisord -c /etc/supervisord.conf
	sudo supervisorctl restart all
	/bin/bash
fi
