#makefile
SHELL := /bin/bash

install: permissions
	@if [ $(env) == local ]; then \
		pip install -r requirements.txt ;\
	elif [ $(env) == production ]; then \
		./conf/cfg.py setup ;\
	fi

clean:
	./conf/cfg.py clean

runserver:
	./conf/cfg.py runserver $(server) $(ini)

collectstatic:
	./conf/cfg.py collectstatic

populate_db:
	./conf/cfg.py populate_db $(settings)

clean_db:
	./conf/cfg.py clean_db

create_db:
	./conf/cfg.py create_db makemigrations,migrate $(settings)

connect:
	./conf/cfg.py connect

create_superuser:
	./conf/cfg.py create_superuser $(settings) syncdb

permissions:
	./conf/cfg.py permissions