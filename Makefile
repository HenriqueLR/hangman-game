#makefile

install:
	pip install -r requirements.txt

clean:
	@find . -name "*.pyc" | xargs rm -f

setup:
	./setup.sh

run_uwsgi:
	./runserver.sh uwsgi

run_gunicorn:
	./runserver.sh gunicorn

collectstatic:
	./app/manage.py collectstatic

populate_db:
	./app/conf/populate_words.py

clean_db:
	@find . -name "*.sqlite3" | xargs rm -f

create_db:
	./app/manage.py makemigrations ;\
	./app/manage.py migrate ;\