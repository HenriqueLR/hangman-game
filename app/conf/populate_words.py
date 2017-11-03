#!/usr/bin/env python
#coding: utf-8

import os, sys, csv, django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_production')
django.setup()

from django.db.utils import IntegrityError
from conf import settings
from main.models import Words



class PopulateDB(object):
	'''
	Import csv file and populate
	base model Words.
	'''
	_total_errors_integrity = 0
	_msg_error_integrity = str()

	def __init__(self):
		self.file_words = settings.FILE_PATH_WORDS

	def insert_word(self, word):
		try:
			return Words(word=word).save()
		except IntegrityError as e:
			self._total_errors_integrity += 1
			self._msg_error_integrity = e.message

	def import_csv_words(self):
		with open(self.file_words, 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
				self.insert_word(row['word'])
		return True


if __name__ == '__main__':
	populate = PopulateDB()
	populate.import_csv_words()
	print ('Total de palavras repetidas: %s\nError: %s') % \
			(populate._total_errors_integrity, populate._msg_error_integrity)

