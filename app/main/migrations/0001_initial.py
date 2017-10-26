# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartGame',
            fields=[
                ('id_start_game', models.AutoField(serialize=False, verbose_name='start_game', primary_key=True, db_column=b'id_start_game')),
                ('word', models.CharField(max_length=30, verbose_name='word', db_column=b'word')),
                ('count_error', models.CharField(max_length=30, verbose_name='count_error', db_column=b'count_error')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
            ],
            options={
                'ordering': ['id_start_game'],
                'db_table': 'start_game',
                'verbose_name': 'StartGame',
                'verbose_name_plural': 'StartGame',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id_words', models.AutoField(serialize=False, verbose_name='words', primary_key=True, db_column=b'id_words')),
                ('word', models.CharField(max_length=30, verbose_name='word', db_column=b'word')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em', db_column=b'updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em', db_column=b'created_at')),
            ],
            options={
                'ordering': ['id_words'],
                'db_table': 'words',
                'verbose_name': 'Word',
                'verbose_name_plural': 'Words',
            },
            bases=(models.Model,),
        ),
    ]
