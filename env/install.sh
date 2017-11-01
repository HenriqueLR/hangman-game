#!/bin/bash -xe

sudo apt-get install -y openssh-server
sudo ./env/config/sys/add-user.sh

sudo apt-get install -y nginx
sudo cp ./env/config/nginx/default /etc/nginx/sites-enabled/default

sudo apt-get install -y curl wget
sudo apt-get install -y python-pip python-dev build-essential freetds-dev

sudo apt-get -y update
sudo apt-get install -y libaio1 psmisc libnuma1 libstdc++6 libjpeg-dev

sudo pip install -r ./requirements.txt

sudo cp ./env/config/supervisord/supervisord.conf /etc/supervisord.conf


sudo ../app/manage.py collectstatic
sudo find ../ -name "*.sqlite3" | xargs rm -f
sudo ../app/manage.py makemigrations
sudo ../app/manage.py migrate
sudo ../app/conf/populate_words.py
