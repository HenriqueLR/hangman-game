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
