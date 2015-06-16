# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0003_auto_20150606_1935'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='rut_user',
        ),
    ]
