#coding: utf-8

import re
from django import forms
from django.utils.translation import ugettext_lazy as _
from main.utils import parse_csv_file as read_file


def _validation_word(word):
	if len(word) > 46:
		raise forms.ValidationError(_('Maximum length allowed 46 words.'))
	if ' ' in word:
		raise forms.ValidationError(_('Forbidden use words with whitespaces.'))
	if not re.match(r'^\w+$', word):
		raise forms.ValidationError(_('Forbidden use words with special character.'))



class FilesAdminForm(forms.ModelForm):

	def clean_file(self):
		file = self.cleaned_data['file']
		parse_file = read_file(file)

		if not 'word' in parse_file.fieldnames:
			raise forms.ValidationError(_('Structure file incorrect, check example in documentation.'))

		for row in parse_file:
			_validation_word(row['word'])

		return file

	class Meta:
		fields = '__all__'



class WordsAdminForm(forms.ModelForm):

	def clean_word(self):
		word = self.cleaned_data['word']
		_validation_word(word)
		return word

	class Meta:
		fields = '__all__'
