#makefile

install:
	pip install -r requirements.txt

clean:
	@find . -name "*.pyc" | xargs rm -f

setup:
	./setup.sh

run:
	./run.sh

collectstatic:
	./app/manage.py collectstatic
