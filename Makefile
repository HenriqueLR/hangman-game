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
	./app/conf/populate_words.py --conf=$(settings) ;\

clean_db: remove_migrations clean
	./conf/cfg.py clean_db

create_db:
	./conf/cfg.py create_db makemigrations,migrate $(settings)

reset_db: clean_db clean_csv_files create_db create_superuser

connect:
	./conf/cfg.py connect

create_superuser:
	./conf/cfg.py create_superuser $(settings) syncdb

permissions:
	./conf/cfg.py permissions

remove_migrations:
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

clean_csv_files:
	find ./app/conf/media/uploads/ -name "*.csv" | xargs rm -f
