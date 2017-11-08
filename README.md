
##### Requisitos

* docker.io

* Chrome browser


##### Instalação

Recomendável que utilize virtualenv

	make setup


##### Start Server

	make run_uwsgi or  make run_gunicorn
	http://localhost


observação:
	Para ativar a aplicação no modo debug e ter a interatividade no console:

		make run
		http://localhost:8008


##### Inserindo palavras no jogo

É possivel inserir palavras no jogo de duas maneiras:

	1 - Carrege um ou mais arquivos dentro do diretório /env/db/

		ex: /env/db/words.csv
		make populate_db

	2 - Acesse a área do administrador

		http://localhost/security


##### Descrição

	Jogo da forca.
