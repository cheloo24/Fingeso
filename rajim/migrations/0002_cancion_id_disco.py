# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cancion',
            name='id_disco',
            field=models.ForeignKey(db_column='ID_DISCO', blank=True, to='rajim.Disco', null=True),
            preserve_default=True,
        ),
    ]
