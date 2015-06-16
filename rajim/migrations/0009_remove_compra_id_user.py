# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0008_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='id_user',
        ),
    ]
