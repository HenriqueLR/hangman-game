#!/bin/bash -xe

sudo /etc/init.d/nginx restart

sudo supervisord -c /etc/supervisord.conf

sudo supervisorctl restart all

/bin/bash
