#coding: utf-8

import os, re, unicodedata, csv
from conf.settings import BASE_DIR, MEDIA_ROOT


def remove_special_word(string):
	'''
	this function return empty word
	specials characters
	'''
	try:
		word = unicode(string, 'utf-8')
	except TypeError as error:
		word = string

	nfkd = unicodedata.normalize('NFKD', word)
	normalize_word = u"".join([c for c in nfkd if not unicodedata.combining(c)])
	return re.sub('[^a-zA-Z0-9 \\\]', '', normalize_word)


def parse_csv_file(file):
	'''
	this function return parse
	csv file
	'''
	return csv.DictReader(file.read().splitlines())


def remove_csv_files(filename):
	'''
	this function remove csv file,
	from path upload.
	'''
	try:
		os.remove(os.path.join(os.path.join(BASE_DIR, MEDIA_ROOT), filename))
	except Exception as e:
		pass