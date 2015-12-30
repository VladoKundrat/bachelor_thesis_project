from django.contrib import admin
from .models import Piece, Album, Arrangement, PieceMovement, Interpret, Composer

class PieceAlbumInline(admin.TabularInline):
    model = Album.piece.through
    extra = 0

class ArrangementInline(admin.TabularInline):
    model = Arrangement
    extra = 0

class PieceMovementInline(admin.TabularInline):
    model = PieceMovement
    extra = 0

class ComposerAlbumInline(admin.TabularInline):
    model = Composer.album.through
    extra = 0

class PieceAdmin(admin.ModelAdmin):
#   pass
    inlines =  [ArrangementInline, PieceMovementInline, PieceAlbumInline]

    list_display = ('piece_id', 'cz_title', 'en_title', 'jw_catalogue_number_part_I', 'jw_catalogue_number_part_II',
                    'time_of_composition','date_of_premiere', 'place_of_premiere', 'compose_for', 'number_of_movement', 'wiki')

    ordering = ('piece_id',)
    list_filter = ['cz_title']
    search_fields = ['cz_title', 'en_title']

class AlbumAdmin(admin.ModelAdmin):

    inlines = [PieceAlbumInline, ComposerAlbumInline, ]
    exclude = ('piece',)
    list_display = ('album_id', 'label_name', 'catalogue_number', 'album_name', 'album_published_year', 'published_country',
                    'number_of_media', 'recording_technology', 'diameter', 'rpm', 'region_code', 'side_coumpling', 'tv_system',
                    'sound_system', 'medium_type', 'subtitles', 'comment', 'text_language', 'text_by', 'note_language', 'note_by',
                    'libretto_language', 'libretto_by')

    ordering = ('album_id',)
    list_filter = ['label_name']
    search_fields = ['catalogue_number']

class ArrangementAdmin(admin.ModelAdmin):

    list_display = ('arrangement_id', 'suitable_for', 'arrangemet_for', 'arrangemet_by', 'perfomr_by', 'piece_id')

    ordering = ('arrangement_id',)
    list_filter = ['suitable_for']
    search_fields = ['arrangement_for']

class PieceMovementAdmin(admin.ModelAdmin):

    list_display = ('piece_movement_id', 'movement_order', 'movement_title', 'piece_id')

    ordering = ('piece_movement_id',)
    list_filter = ['piece_id']
    search_fields = ['movement_title']

class InterpretAdmin(admin.ModelAdmin):

    list_display = ('interpret_id', 'interpret_name')

    ordering = ('interpret_id',)
    list_filter = ['interpret_name']
    search_fields = ['interpret_name']

class ComposerAdmin(admin.ModelAdmin):

    inlines = [ComposerAlbumInline, ]
    list_display = ('id', 'composer_name')

    ordering = ('id',)
    list_filter = ['composer_name']
    search_fields = ['composer_name']


admin.site.register(Piece, PieceAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Arrangement, ArrangementAdmin)
admin.site.register(PieceMovement, PieceMovementAdmin)
admin.site.register(Interpret, InterpretAdmin)
admin.site.register(Composer, ComposerAdmin)

