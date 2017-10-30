#!/bin/bash -xe

sudo /etc/init.d/nginx restart

sudo uwsgi --ini /deploy/apps/hangman-game/env/res/local.ini --logto uwsgi.log
