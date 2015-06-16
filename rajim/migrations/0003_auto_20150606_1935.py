# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0002_cancion_id_disco'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='tiene',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='tiene',
            name='id_cancion',
        ),
        migrations.RemoveField(
            model_name='tiene',
            name='id_disco',
        ),
        migrations.DeleteModel(
            name='Tiene',
        ),
    ]
