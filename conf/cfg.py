#!/usr/bin/env python
#coding: utf-8

import importlib, os, sys, commands
from ConfigParser import RawConfigParser



def init_parser_config(file=None):
	config = RawConfigParser()
	if not file:
		path = os.path.dirname(os.path.abspath(__file__))
		command = ('%s %s %s') % ('find', path, '-name "*.conf.ini"')
		status, file = commands.getstatusoutput(command)
	config.read(file)
	return config

def _get_commands(config, arg):
	method = arg[1]
	param = arg[2:]
	module_class = importlib.import_module('cfg')
	clazz = getattr(module_class, config.get('conf', 'CLASS_NAME'))
	call = getattr(clazz(config), method.lower())
	return call(param)



class Commands(object):

	def __init__(self, config):
		self.config = config

	def setup(self, *args, **kwargs):
		file = self.config.get('hangman', 'SETUP_SH')
		image = self.config.get('hangman', 'IMAGE')
		img_version = self.config.get('hangman', 'IMG_VERSION')
		param = ('%s %s') % (image, img_version)
		command = ('%s%s %s') % ('./', file, param)
		self.exec_command(command)

	def populate_db(self, *args, **kwargs):
		args = args[0]
		path = self.config.get('conf', 'PATH_CONF')
		file = self.config.get('conf', 'POPULATE_SCRIPT')
		param = ('%s %s') % ('-c', self.config.get('app','SETTINGS_'+args[0].upper()))
		command = ('%s%s%s %s') % ('./', path, file, param)
		self.exec_command(command)

	def create_superuser(self, *args, **kwargs):
		args = args[0]
		path = self.config.get('app', 'PATH')
		file = self.config.get('app', 'MANAGE_SCRIPT')
		param = ('%s%s') % ('--settings=conf.', self.config.get('app','SETTINGS_'+args[0].upper()))
		command = ('%s%s%s %s %s') % ('./', path, file, args[1].lower(), param)
		self.exec_command(command)

	def runserver(self, *args, **kwargs):
		args = args[0]
		if args[0] in ['uwsgi', 'gunicorn']:
			file = self.config.get('hangman', 'RUNSERVER_SH')
			image = self.config.get('hangman', 'IMAGE')
			img_version = self.config.get('hangman', 'IMG_VERSION')
			workdir = ''.join(['/', self.config.get('hangman', 'WORKDIR')])
			port = self.config.get('hangman', args[0].upper()+'_PORT')
			path = ''.join(['./', self.config.get('env', 'PATH')])
			services = self.config.get('env', 'SERVICES_SCRIPT')
			path_services = ''.join([path, services])
			opt = self.config.get('hangman', args[0].upper()+'_OPT')
			param = ('%s %s %s %s %s %s %s %s') % (args[0].lower(), args[1].lower(), image,
												img_version, workdir, port, path_services, opt)
			command = ('%s%s %s') % ('./', file, param)
			self.exec_command(command)

		elif args[0] == 'local':
			file = self.config.get('app', 'MANAGE_SCRIPT')
			port = self.config.get('app', 'PORT')
			path = self.config.get('app', 'PATH')
			param = ('%s %s') % (self.config.get('app', 'LOCAL'), port)
			file_path = ''.join([path, file])
			command = ('%s%s %s') % ('./', file_path, param)
			self.exec_command(command)

	def collectstatic(self, *args, **kwargs):
		file = self.config.get('app', 'MANAGE_SCRIPT')
		path = self.config.get('app', 'PATH')
		file_path = ''.join([path, file])
		param = self.config.get('app', 'STATIC_CMD')
		command = ('%s%s %s') % ('./', file_path, param)
		self.exec_command(command)

	def clean_db(self, *args, **kwargs):
		db = self.config.get('app', 'DB')
		command = 'find . -name "*.'+db+'" | xargs rm -f'
		self.exec_command(command)

	def clean(self, *args, **kwargs):
		command = 'find . -name "*.pyc" | xargs rm -f'
		self.exec_command(command)

	def create_db(self, *args, **kwargs):
		args = args[0]
		file = self.config.get('app', 'MANAGE_SCRIPT')
		path = self.config.get('app', 'PATH')
		file_path = ''.join([path, file])
		settings = ('%s%s') % ('--settings=conf.', self.config.get('app','SETTINGS_'+args[1].upper()))
		makemigrate, migrate = args[0].split(",")

		for param in [makemigrate, migrate]:
			command = ('%s%s %s %s') % ('./', file_path, param, settings)
			self.exec_command(command)

	def connect(self, *args, **kwargs):
		file = self.config.get('env', 'CONNECT_SH')
		path = self.config.get('env', 'PATH')
		file_path = ''.join([path, file])
		image = self.config.get('hangman', 'IMAGE')
		command = ('%s%s %s') % ('./', file_path, image)
		self.exec_command(command)

	def permissions(self, *args, **kwargs):
		file = __file__
		command = ('%s %s') % ('chmod 0755', file)
		self.exec_command(command)
		command = 'find . -name "*.sh" | xargs chmod 0755'
		self.exec_command(command)

	def exec_command(self, command):
		os.system(command)



if __name__ == '__main__':
	config = init_parser_config()
	_get_commands(config, sys.argv)
