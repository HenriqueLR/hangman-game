#coding: utf-8

import unicodedata
import re



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
