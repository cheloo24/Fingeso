# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0006_auto_20150611_0126'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
