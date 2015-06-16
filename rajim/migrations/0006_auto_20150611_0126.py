# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rajim.models


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0005_disco_caratula'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disco',
            name='caratula',
            field=models.ImageField(upload_to=rajim.models.url),
            preserve_default=True,
        ),
    ]
