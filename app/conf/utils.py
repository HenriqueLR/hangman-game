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
