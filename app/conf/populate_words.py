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
from utils import WordFile



class PopulateDB(object):
	'''
	Import csv file and populate
	base model Words.
	'''
	_total_errors_integrity = 0
	_msg_error_integrity = str()

	def __init__(self):
		self.config_word = WordFile()

	def insert_word(self, word):
		try:
			return Words(word=word).save()
		except IntegrityError as e:
			self._total_errors_integrity += 1
			self._msg_error_integrity = e.message

	def import_csv_words(self):
		for file in self.config_word.get_files():
			with open(''.join([self.config_word.get_path(), file]), 'r') as f:
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