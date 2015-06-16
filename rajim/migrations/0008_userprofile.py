# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import rajim.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rajim', '0007_disco_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='userProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo', models.ImageField(upload_to=rajim.models.url2)),
                ('fecha_nacimiento_user', models.DateField(null=True, db_column='FECHA_NACIMIENTO_USER', blank=True)),
                ('descuento', models.IntegerField(null=True, db_column='DESCUENTO', blank=True)),
                ('direccion', models.CharField(max_length=40, null=True, db_column='DIRECCION', blank=True)),
                ('valoracion_user', models.IntegerField(null=True, db_column='VALORACION_USER', blank=True)),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
