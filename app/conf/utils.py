#coding: utf-8

import os, commands
from ConfigParser import RawConfigParser
from settings import BASE_DIR



def init_parser_config(file=None):
	config = RawConfigParser()
	if not file:
		path = os.path.dirname(os.path.dirname(BASE_DIR))
		command = ('%s %s %s') % ('find', path, '-name "*.conf.ini"')
		status, file = commands.getstatusoutput(command)
	config.read(file)
	return config



class WordFile(object):
	def __init__(self):
		self.config = init_parser_config()

	def get_path(self):
		return os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)),
							self.config.get('env', 'PATH_DB'))

	def get_files(self):
		return filter(lambda x: x.endswith('.csv'), os.listdir(self.get_path()))
