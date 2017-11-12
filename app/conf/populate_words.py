#!/usr/bin/env python
#coding: utf-8

import os, sys, csv, django, argparse

parser = argparse.ArgumentParser(description='Populate words csv file in database')
parser.add_argument('-c', '--conf', dest='settings', help='name settings file ex: settings')
args = parser.parse_args()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', args.settings)
django.setup()

from django.db.utils import IntegrityError
from main.models import Words
from utils import init_parser_config
from settings import BASE_DIR



class PopulateDB(object):
	'''
	Import csv file and populate
	base model Words.
	'''
	_total_errors_integrity = 0
	_msg_error_integrity = str()

	def __init__(self):
		self.config = init_parser_config()

	def get_path(self):
		return os.path.join(os.path.dirname(os.path.dirname(BASE_DIR)),
							self.config.get('env', 'PATH_DB'))

	def get_files(self):
		return filter(lambda x: x.endswith('.csv'), os.listdir(self.get_path()))

	def insert_word(self, word):
		try:
			return Words(word=word).save()
		except IntegrityError as e:
			self._total_errors_integrity += 1
			self._msg_error_integrity = e.message

	def import_csv_words(self):
		for file in self.get_files():
			with open(''.join([self.get_path(), file]), 'r') as f:
				reader = csv.DictReader(f)
				for row in reader:
					self.insert_word(row['word'])
		return True


if __name__ == '__main__':
	try:
		print 'Db file in: ' + os.environ['DJANGO_SETTINGS_MODULE']
		populate = PopulateDB()
		populate.import_csv_words()

		if populate._total_errors_integrity:
			print ('Total de palavras repetidas: %s\nError: %s') % \
				(populate._total_errors_integrity, populate._msg_error_integrity)
	except Exception as error:
		print error
		pass