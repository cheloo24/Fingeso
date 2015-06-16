# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0009_remove_compra_id_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco',
            name='resena',
            field=models.TextField(max_length=1024, null=True, db_column='RESENA', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='artista',
            name='resena',
            field=models.TextField(max_length=1024, null=True, db_column='RESENA', blank=True),
            preserve_default=True,
        ),
    ]
