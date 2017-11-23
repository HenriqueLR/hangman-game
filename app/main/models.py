#coding: utf-8

from django.db import models, transaction
from django.db.models.signals import post_save
from django.db.utils import IntegrityError
from django.dispatch import receiver
from main.utils import remove_special_word, parse_csv_file
from main.validators import ContentTypeRestrictedFileField
from conf.settings import MAX_UPLOAD_SIZE, CONTENT_TYPES, EXT



class Words(models.Model):

	id_words = models.AutoField(primary_key=True, verbose_name=u'words', db_column='id_words')
	word = models.CharField(verbose_name=u'word', db_column='word', max_length=46, unique=True)
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')

	def __unicode__(self):
		return (u'%s') % (self.word)

	def save(self, *args, **kwargs):
		self.word = remove_special_word(self.word)
		super(Words, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Word'
		verbose_name_plural = 'Words'
		ordering=['-id_words']
		db_table='words'



class Files(models.Model):

	id_file = models.AutoField(primary_key=True, verbose_name=u'file', db_column='id_file')
	file = ContentTypeRestrictedFileField(
		upload_to='uploads/',
		content_types=CONTENT_TYPES,
		max_upload_size=MAX_UPLOAD_SIZE,
		extensions=EXT
    )
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')

	def __unicode__(self):
		return (u'%s') % (self.file)

	class Meta:
		verbose_name = 'File'
		verbose_name_plural = 'Files'
		ordering=['-id_file']
		db_table='files'



@receiver(post_save, sender=Files)
def populate_words(sender, instance, *args, **kwargs):
	for row in parse_csv_file(instance.file):
		try:
			with transaction.atomic():
				Words(word=row['word']).save()
		except IntegrityError as e:
			pass
		except Exception as e:
			pass
