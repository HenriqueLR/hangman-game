
##### Requisitos

* Linux
	* Python 2.7
	* docker.io
	* Chrome browser

A instalação do docker.io somente é necessário, para o ambiente de produção,
para fazer testes, alterações no código da aplicação não é obrigatório.


##### Instalação

Recomendações:

* virtualenv
* rodar os comandos como superusuario do sistema

production: - (obrigatório a instalação do docker.io)

	make install env=production

development:

	make install env=local


##### Start Server

Aplicação tem suporte para (uwsgi / gunicorn), recomendado para ambientes de produção,
e para desenvolvimento local o manage do django.

production:

A diferença entre ini=local or ini=production, é que no modo local
ativa o debug dos requests.

	make runserver server=uwsgi ini=local or ini=production
	or
	make runserver server=gunicorn ini=local or ini=production

	http://localhost

development:

	make runserver server=local
	http://localhost:8008


##### Inserindo palavras no jogo

É possivel inserir palavras no jogo de duas maneiras:

	1 - Carrege um ou mais arquivos como de
		exemplo dentro do diretório /env/db/

		ex: /env/db/words.csv
		make populate_db

	2 - Acesse a área do administrador
		http://localhost/security - (production)*
		http://localhost:8008/security - (local)*
		login: root
		senha: root


##### Comandos

make clean
	remove os arquivos .pyc dos diretorios do projeto

make collectstatic
	coleta os arquivos statics do projeto para /app/conf/static_files/

make populate_db settings=[local/production]
	ex: make populate_db settings=production
	carrega palavras usando arquivo especificado no settings

make clean_db
	remove o banco local

make create_db settings=[local/production]
	ex: make create_db settings=local
	cria o banco usando o arquivo especificado no settings

make connect
	conecta no docker container

make create_superuser settings=[local/production]
	ex: make create_superuser settings=local
	cria o usuario no banco usando o arquivo especificado no settings

make permissions
	muda as permissões dos arquivos cfg.py / *.sh


##### Descrição

	Jogo da forca.
