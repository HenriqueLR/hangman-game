from django.db import models



class Words(models.Model):

	id_words = models.AutoField(primary_key=True, verbose_name=u'words', db_column='id_words')
	word = models.CharField(verbose_name=u'word', db_column='word', max_length=30)
	updated_at = models.DateTimeField(verbose_name=u'Atualizado em', auto_now=True, db_column='updated_at')
	created_at = models.DateTimeField(verbose_name=u'Criado em', auto_now_add=True, db_column='created_at')

	def __unicode__(self):
		return (u'%s') % (self.word)

	class Meta:
		verbose_name = 'Word'
		verbose_name_plural = 'Words'
		ordering=['id_words']
		db_table='words'