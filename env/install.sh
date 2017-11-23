#!/bin/bash -xe

sudo apt-get -y update \
&& apt-get install -y openssh-server \
&& ./env/sys/add-user.sh \
&& apt-get install -y nginx \
&& cp ./env/nginx/default /etc/nginx/sites-enabled/default \
&& apt-get install -y curl wget \
&& apt-get install -y python-pip python-dev build-essential freetds-dev \
&& apt-get install -y libaio1 psmisc libnuma1 libstdc++6 libjpeg-dev \
&& pip install -r ./requirements.txt \
&& cp ./env/supervisord/supervisord.conf /etc/supervisord.conf \
&& find . -name "*.sqlite3" | xargs rm -f \
&& find . -path "*/migrations/*.py" -not -name "__init__.py" -delete \
&& find . -name "*.pyc" | xargs rm -f \
&& ./app/manage.py collectstatic --noinput \
&& ./app/manage.py makemigrations --settings=conf.settings_production \
&& ./app/manage.py migrate --settings=conf.settings_production \
&& ./app/conf/populate_words.py --conf=settings_production
