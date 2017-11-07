
##### Requisitos

	docker.io

	Chrome browser


##### Instalação

	make setup


##### Start Server

	make run_uwsgi or  make run_gunicorn
	http://localhost

	runserver local interactive:
		make run
		http://localhost:8008


##### Inserindo palavras no jogo

	Carrege um arquivo como de exemplo /env/db/words.csv
	make populate_db

	http://localhost/security


##### Descrição

	Jogo da forca.
