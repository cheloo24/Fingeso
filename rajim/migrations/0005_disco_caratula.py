# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rajim.models


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0004_remove_usuario_rut_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='disco',
            name='caratula',
            field=models.ImageField(default='../static/Fingeso/images/bg.jpg', upload_to=rajim.models.url),
            preserve_default=True,
        ),
    ]
