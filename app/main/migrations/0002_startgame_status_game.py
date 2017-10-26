# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='startgame',
            name='status_game',
            field=models.BooleanField(default=True, verbose_name='status_game', db_column=b'status_game'),
            preserve_default=True,
        ),
    ]
