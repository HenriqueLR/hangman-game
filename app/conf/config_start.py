#!/usr/bin/env python
#coding: utf-8

import os, sys, django, argparse

parser = argparse.ArgumentParser(description='Create superuser')
parser.add_argument('-c', '--conf', dest='settings', help='name settings file ex: settings')
args = parser.parse_args()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', args.settings)
django.setup()

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from utils import init_parser_config



class ConfigStart(object):
	'''
	Created super user.
	'''
	def __init__(self):
		self.user_model = get_user_model()
		self.config = init_parser_config()

	def create_user(self):
		user = self.user_model(email=self.config.get('app', 'EMAIL'),
							   password=make_password(self.config.get('app', 'PASSWORD')),
							   username=self.config.get('app', 'USERNAME'))
		user.is_staff = True
		user.is_superuser = True
		user.is_active = True
		user.save()
		return user


if __name__ == '__main__':
	try:
		print 'Db file in: ' + os.environ['DJANGO_SETTINGS_MODULE']
		user = ConfigStart().create_user()
		print 'user created: %s' % (user.username)
	except Exception as Error:
		print Error
		pass
