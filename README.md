
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


Criar o superusuario do sistema, é obrigatório para acessar,
a interface  de administração do sistema.

	make create_superuser settings=local


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

	1 - Carrege um ou mais arquivos como de exemplo '/env/db/words.csv',
		dentro do diretório '/app/conf/static/uploads/file.csv'

		ex: /app/conf/static/uploads/words.csv
		make populate_db

	2 - Acesse a área do administrador
		http://localhost/security - (production)*
		http://localhost:8008/security - (local)*


##### Comandos

1 - make clean

* remove os arquivos .pyc dos diretorios do projeto

2 - make collectstatic

* coleta os arquivos statics do projeto para /app/conf/static_files/

3 - make populate_db settings=[local/production]

	ex: make populate_db settings=production
	carrega palavras usando arquivo especificado no settings

4 - make clean_db

* remove o banco local

5 - make create_db settings=[local/production]

	ex: make create_db settings=local
	cria o banco usando o arquivo especificado no settings

6 - make connect

* conecta no docker container

7 - make create_superuser settings=[local/production]

	ex: make create_superuser settings=local
	cria o usuario no banco usando o arquivo especificado no settings

8 - make permissions

* muda as permissões dos arquivos cfg.py / *.sh


##### Descrição

	Jogo da forca.
