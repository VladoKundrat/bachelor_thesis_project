from django.db import models

class Piece(models.Model):
    piece_id = models.IntegerField(primary_key=True)
    cz_title = models.CharField(max_length=255, blank=True, null=True)
    en_title = models.CharField(max_length=255, blank=True, null=True)
    jw_catalogue_number_part_I = models.CharField(max_length=255, blank=True, null=True)
    jw_catalogue_number_part_II = models.CharField(max_length=255, blank=True, null=True)
    time_of_composition = models.CharField(max_length=255, blank=True, null=True)
    date_of_premiere = models.CharField(max_length=255, blank=True, null=True)
    place_of_premiere = models.CharField(max_length=255, blank=True, null=True)
    compose_for = models.CharField(max_length=255, blank=True, null=True)
    number_of_movement = models.CharField (max_length=255, blank=True, null=True)
    wiki = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.cz_title

class Arrangement(models.Model):
    arrangement_id = models.IntegerField(primary_key=True)
    suitable_for = models.CharField(max_length=255, blank=True, null=True)
    arrangemet_for = models.CharField(max_length=255, blank=True, null=True)
    arrangemet_by = models.CharField(max_length=255, blank=True, null=True)
    perfomr_by = models.CharField(max_length=255, blank=True, null=True)
    piece = models.ForeignKey(Piece)

    def __unicode__(self):
        return self.suitable_for

class PieceMovement(models.Model):
    piece_movement_id = models.IntegerField(primary_key=True)
    movement_order = models.IntegerField(blank=True, null=True)
    movement_title = models.CharField(max_length=255, blank=True, null=True)
    piece = models.ForeignKey(Piece)

    def __unicode__(self):
        return self.movement_title

class Album(models.Model):
    album_id = models.IntegerField(primary_key=True)
    label_name = models.CharField(max_length=255, blank=True, null=True)
    catalogue_number = models.CharField(max_length=255, blank=True, null=True)
    album_name = models.CharField(max_length=255, blank=True, null=True)
    album_published_year = models.CharField(max_length=255, blank=True, null=True)
    published_country = models.CharField(max_length=255, blank=True, null=True)
    number_of_media = models.CharField(max_length=255, blank=True, null=True)
    recording_technology = models.CharField(max_length=255, blank=True, null=True)
    side_coumpling = models.CharField(max_length=255, blank=True, null=True)
    diameter = models.CharField(max_length=255, blank=True, null=True)
    rpm = models.CharField(max_length=255, blank=True, null=True)
    tv_system = models.CharField(max_length=255, blank=True, null=True)
    region_code = models.CharField(max_length=255, blank=True, null=True)
    sound_system = models.CharField(max_length=255, blank=True, null=True)
    medium_type = models.CharField(max_length=255, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)
    subtitles = models.CharField(max_length=255, blank=True, null=True)
    text_language = models.CharField(max_length=255, blank=True, null=True)
    text_by = models.CharField(max_length=255, blank=True, null=True)
    note_language = models.CharField(max_length=255, blank=True, null=True)
    note_by = models.CharField(max_length=255, blank=True, null=True)
    libretto_language = models.CharField(max_length=255, blank=True, null=True)
    libretto_by = models.CharField(max_length=255, blank=True, null=True)
    catalogue_number_LJF = models.CharField(max_length=255, blank=True, null=True)
    piece = models.ManyToManyField(Piece, through='AlbumPiece', through_fields=('album', 'piece'))


    def __unicode__(self):
        return self.label_name

    def __unicode__(self):
        return self.album_name

    def __unicode__(self):
        return self.catalogue_number

class Interpret(models.Model):
    interpret_id = models.IntegerField(primary_key=True)
    interpret_name = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        return self.interpret_name

class AlbumPiece (models.Model):
    album = models.ForeignKey(Album)
    piece = models.ForeignKey(Piece)
    interpret = models.ForeignKey(Interpret)
    year_of_recording = models.CharField(max_length=250, blank=True, null=True)
    track_order = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return str(self.album)

class Composer(models.Model):
    composer_name = models.CharField(max_length=255, blank=True, null=True)
    album = models.ManyToManyField(Album, through='ComposerAlbum', through_fields=('composer', 'album'))

    def __unicode__(self):
        return self.composer_name

class ComposerAlbum(models.Model):
    composer = models.ForeignKey(Composer)
    album = models.ForeignKey(Album)


