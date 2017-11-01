#!/usr/bin/env python
#coding: utf-8

import os, sys
import csv
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings_production')
django.setup()

from conf import settings
from main.models import Words


class PopulateDB(object):
	'''
	import csv file and populate
	base model in sqlite3
	'''
	def __init__(self):
		self.file_words = settings.FILE_PATH_WORDS

	def insert_word(self, word):
		return Words(word=word).save()

	def import_csv_words(self):
		with open(self.file_words, 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
				self.insert_word(row['word'])
		return True

if __name__ == '__main__':
	try:
		PopulateDB().import_csv_words()
	except Exception as Error:
		print Error
		pass