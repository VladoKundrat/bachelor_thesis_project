# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.IntegerField(serialize=False, primary_key=True)),
                ('label_name', models.CharField(max_length=255, null=True, blank=True)),
                ('catalogue_number', models.CharField(max_length=255, null=True, blank=True)),
                ('album_name', models.CharField(max_length=255, null=True, blank=True)),
                ('album_published_year', models.CharField(max_length=255, null=True, blank=True)),
                ('published_country', models.CharField(max_length=255, null=True, blank=True)),
                ('number_of_media', models.CharField(max_length=255, null=True, blank=True)),
                ('recording_technology', models.CharField(max_length=255, null=True, blank=True)),
                ('side_coumpling', models.CharField(max_length=255, null=True, blank=True)),
                ('diameter', models.CharField(max_length=255, null=True, blank=True)),
                ('rpm', models.CharField(max_length=255, null=True, blank=True)),
                ('tv_system', models.CharField(max_length=255, null=True, blank=True)),
                ('region_code', models.CharField(max_length=255, null=True, blank=True)),
                ('sound_system', models.CharField(max_length=255, null=True, blank=True)),
                ('medium_type', models.CharField(max_length=255, null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('subtitles', models.CharField(max_length=255, null=True, blank=True)),
                ('text_language', models.CharField(max_length=255, null=True, blank=True)),
                ('text_by', models.CharField(max_length=255, null=True, blank=True)),
                ('note_language', models.CharField(max_length=255, null=True, blank=True)),
                ('note_by', models.CharField(max_length=255, null=True, blank=True)),
                ('libretto_language', models.CharField(max_length=255, null=True, blank=True)),
                ('libretto_by', models.CharField(max_length=255, null=True, blank=True)),
                ('catalogue_number_LJF', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='AlbumPiece',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year_of_recording', models.CharField(max_length=250, null=True, blank=True)),
                ('track_order', models.CharField(max_length=250, null=True, blank=True)),
                ('album', models.ForeignKey(to='database_of_janacek_works.Album')),
            ],
        ),
        migrations.CreateModel(
            name='Arrangement',
            fields=[
                ('arrangement_id', models.IntegerField(serialize=False, primary_key=True)),
                ('suitable_for', models.CharField(max_length=255, null=True, blank=True)),
                ('arrangemet_for', models.CharField(max_length=255, null=True, blank=True)),
                ('arrangemet_by', models.CharField(max_length=255, null=True, blank=True)),
                ('perfomr_by', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('composer_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ComposerAlbum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album', models.ForeignKey(to='database_of_janacek_works.Album')),
                ('composer', models.ForeignKey(to='database_of_janacek_works.Composer')),
            ],
        ),
        migrations.CreateModel(
            name='Interpret',
            fields=[
                ('interpret_id', models.IntegerField(serialize=False, primary_key=True)),
                ('interpret_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('piece_id', models.IntegerField(serialize=False, primary_key=True)),
                ('cz_title', models.CharField(max_length=255, null=True, blank=True)),
                ('en_title', models.CharField(max_length=255, null=True, blank=True)),
                ('jw_catalogue_number_part_I', models.CharField(max_length=255, null=True, blank=True)),
                ('jw_catalogue_number_part_II', models.CharField(max_length=255, null=True, blank=True)),
                ('time_of_composition', models.CharField(max_length=255, null=True, blank=True)),
                ('date_of_premiere', models.CharField(max_length=255, null=True, blank=True)),
                ('place_of_premiere', models.CharField(max_length=255, null=True, blank=True)),
                ('compose_for', models.CharField(max_length=255, null=True, blank=True)),
                ('number_of_movement', models.CharField(max_length=255, null=True, blank=True)),
                ('wiki', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PieceMovement',
            fields=[
                ('piece_movement_id', models.IntegerField(serialize=False, primary_key=True)),
                ('movement_order', models.IntegerField(null=True, blank=True)),
                ('movement_title', models.CharField(max_length=255, null=True, blank=True)),
                ('piece', models.ForeignKey(to='database_of_janacek_works.Piece')),
            ],
        ),
        migrations.AddField(
            model_name='composer',
            name='album',
            field=models.ManyToManyField(to='database_of_janacek_works.Album', through='database_of_janacek_works.ComposerAlbum'),
        ),
        migrations.AddField(
            model_name='arrangement',
            name='piece',
            field=models.ForeignKey(to='database_of_janacek_works.Piece'),
        ),
        migrations.AddField(
            model_name='albumpiece',
            name='interpret',
            field=models.ForeignKey(to='database_of_janacek_works.Interpret'),
        ),
        migrations.AddField(
            model_name='albumpiece',
            name='piece',
            field=models.ForeignKey(to='database_of_janacek_works.Piece'),
        ),
        migrations.AddField(
            model_name='album',
            name='piece',
            field=models.ManyToManyField(to='database_of_janacek_works.Piece', through='database_of_janacek_works.AlbumPiece'),
        ),
    ]
