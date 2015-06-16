# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id_admin', models.AutoField(serialize=False, primary_key=True, db_column='ID_ADMIN')),
                ('email_admin', models.CharField(max_length=100, null=True, db_column='EMAIL_ADMIN', blank=True)),
                ('pass_admin', models.CharField(max_length=50, null=True, db_column='PASS_ADMIN', blank=True)),
            ],
            options={
                'db_table': 'administrador',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id_artista', models.AutoField(serialize=False, primary_key=True, db_column='ID_ARTISTA')),
                ('nombre_artista', models.CharField(max_length=60, null=True, db_column='NOMBRE_ARTISTA', blank=True)),
                ('resena', models.CharField(max_length=1024, null=True, db_column='RESENA', blank=True)),
                ('fecha_nacimiento_artista', models.DateField(null=True, db_column='FECHA_NACIMIENTO_ARTISTA', blank=True)),
                ('valoracion_artista', models.IntegerField(null=True, db_column='VALORACION_ARTISTA', blank=True)),
            ],
            options={
                'db_table': 'artista',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id_cancion', models.AutoField(serialize=False, primary_key=True, db_column='ID_CANCION')),
                ('nombre_cancion', models.CharField(max_length=60, null=True, db_column='NOMBRE_CANCION', blank=True)),
                ('duracion', models.IntegerField(null=True, db_column='DURACION', blank=True)),
                ('val_cancion', models.IntegerField(null=True, db_column='VAL_CANCION', blank=True)),
            ],
            options={
                'db_table': 'cancion',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ComentaValoraArtista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_coment_usr_art', models.CharField(max_length=200, null=True, db_column='TEXT_COMENT_USR_ART', blank=True)),
                ('val_usr_artist', models.IntegerField(null=True, db_column='VAL_USR_ARTIST', blank=True)),
                ('id_artista', models.ForeignKey(to='rajim.Artista', db_column='ID_ARTISTA')),
            ],
            options={
                'db_table': 'comenta_valora_artista',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ComentaValoraDisco',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_coment_usr_disc', models.CharField(max_length=200, null=True, db_column='TEXT_COMENT_USR_DISC', blank=True)),
                ('val_usr_disc', models.IntegerField(null=True, db_column='VAL_USR_DISC', blank=True)),
            ],
            options={
                'db_table': 'comenta_valora_disco',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ComentaValoraUsuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text_coment_usr_usr', models.CharField(max_length=200, null=True, db_column='TEXT_COMENT_USR_USR', blank=True)),
                ('val_usr_usr', models.IntegerField(null=True, db_column='VAL_USR_USR', blank=True)),
            ],
            options={
                'db_table': 'comenta_valora_usuario',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id_compra', models.AutoField(serialize=False, primary_key=True, db_column='ID_COMPRA')),
                ('fecha_compra', models.DateTimeField(null=True, db_column='FECHA_COMPRA', blank=True)),
                ('precio_final', models.IntegerField(null=True, db_column='PRECIO_FINAL', blank=True)),
                ('tipo_pago', models.CharField(max_length=10, null=True, db_column='TIPO_PAGO', blank=True)),
            ],
            options={
                'db_table': 'compra',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Disco',
            fields=[
                ('id_disco', models.AutoField(serialize=False, primary_key=True, db_column='ID_DISCO')),
                ('nombre_disco', models.CharField(max_length=60, null=True, db_column='NOMBRE_DISCO', blank=True)),
                ('fecha_lanzamiento', models.DateField(null=True, db_column='FECHA_LANZAMIENTO', blank=True)),
                ('genero', models.CharField(max_length=100, null=True, db_column='GENERO', blank=True)),
                ('valoracion_disco', models.IntegerField(null=True, db_column='VALORACION_DISCO', blank=True)),
                ('precio', models.IntegerField(null=True, db_column='PRECIO', blank=True)),
                ('id_artista', models.ForeignKey(db_column='ID_ARTISTA', blank=True, to='rajim.Artista', null=True)),
                ('id_compra', models.ForeignKey(db_column='ID_COMPRA', blank=True, to='rajim.Compra', null=True)),
            ],
            options={
                'db_table': 'disco',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Tiene',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_cancion', models.ForeignKey(to='rajim.Cancion', db_column='ID_CANCION')),
                ('id_disco', models.ForeignKey(to='rajim.Disco', db_column='ID_DISCO')),
            ],
            options={
                'db_table': 'tiene',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(serialize=False, primary_key=True, db_column='ID_USER')),
                ('nombre_user', models.CharField(max_length=60, null=True, db_column='NOMBRE_USER', blank=True)),
                ('rut_user', models.CharField(max_length=20, null=True, db_column='RUT_USER', blank=True)),
                ('email_user', models.CharField(max_length=100, null=True, db_column='EMAIL_USER', blank=True)),
                ('fecha_nacimiento_user', models.DateField(null=True, db_column='FECHA_NACIMIENTO_USER', blank=True)),
                ('pass_user', models.CharField(max_length=20, null=True, db_column='PASS_USER', blank=True)),
                ('descuento', models.IntegerField(null=True, db_column='DESCUENTO', blank=True)),
                ('direccion', models.CharField(max_length=40, null=True, db_column='DIRECCION', blank=True)),
                ('valoracion_user', models.IntegerField(null=True, db_column='VALORACION_USER', blank=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='compra',
            name='id_disco',
            field=models.ForeignKey(db_column='ID_DISCO', blank=True, to='rajim.Disco', null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='id_user',
            field=models.ForeignKey(db_column='ID_USER', blank=True, to='rajim.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='comentavalorausuario',
            name='comenta_valora_usuario',
            field=models.ForeignKey(to='rajim.Usuario', db_column='COMENTA_VALORA_USUARIO'),
        ),
        migrations.AddField(
            model_name='comentavalorausuario',
            name='id_user',
            field=models.ForeignKey(related_name='comentavalorausuario_usuario_comenta', db_column='ID_USER', to='rajim.Usuario'),
        ),
        migrations.AddField(
            model_name='comentavaloradisco',
            name='id_disco',
            field=models.ForeignKey(to='rajim.Disco', db_column='ID_DISCO'),
        ),
        migrations.AddField(
            model_name='comentavaloradisco',
            name='id_user',
            field=models.ForeignKey(to='rajim.Usuario', db_column='ID_USER'),
        ),
        migrations.AddField(
            model_name='comentavaloraartista',
            name='id_user',
            field=models.ForeignKey(to='rajim.Usuario', db_column='ID_USER'),
        ),
        migrations.AlterUniqueTogether(
            name='tiene',
            unique_together=set([('id_disco', 'id_cancion')]),
        ),
        migrations.AlterUniqueTogether(
            name='comentavalorausuario',
            unique_together=set([('id_user', 'text_coment_usr_usr')]),
        ),
        migrations.AlterUniqueTogether(
            name='comentavaloradisco',
            unique_together=set([('id_user', 'id_disco')]),
        ),
        migrations.AlterUniqueTogether(
            name='comentavaloraartista',
            unique_together=set([('id_user', 'id_artista')]),
        ),
    ]
