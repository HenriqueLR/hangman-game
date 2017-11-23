#coding: utf-8

from django.db.models import FileField
from django.forms import forms
from django.template.defaultfilters import filesizeformat
from django.utils.translation import ugettext_lazy as _



class ContentTypeRestrictedFileField(FileField):
	"""
	Same as FileField, but you can specify:
	* content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
	* max_upload_size - a number indicating the maximum file size allowed for upload listing with values
	  in conf/settings.py.
	* extensions - Example: ['csv', 'txt']
	"""
	def __init__(self, extensions=None, content_types=None, max_upload_size=None, **kwargs):
		self.content_types = content_types
		self.max_upload_size = max_upload_size
		self.extensions = extensions

		super(ContentTypeRestrictedFileField, self).__init__(**kwargs)

	def clean(self, *args, **kwargs):
		data = super(ContentTypeRestrictedFileField, self).clean(*args, **kwargs)
		file = data.file

		try:
			if file.name.split('.')[1] not in self.extensions:
				raise forms.ValidationError(_('File type not supported. Accepted types are: %s.' % ', '.join(self.extensions)))
			elif file.content_type in self.content_types:
				if file._size > self.max_upload_size:
					raise forms.ValidationError(_('Please keep filesize under %s. Current filesize %s.') % (filesizeformat(self.max_upload_size), filesizeformat(file._size)))
			else:
				raise forms.ValidationError(_('Filetype not supported.'))
		except AttributeError:
			pass

		return data
