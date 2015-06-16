# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import likert_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('rajim', '0011_comentadisco_valoradisco'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetShopSurvey',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_like_snakes', likert_field.models.LikertField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
