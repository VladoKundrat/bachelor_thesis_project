from django.shortcuts import render_to_response
from django.views import generic
from django_datatables_view.base_datatable_view import BaseDatatableView
from database_of_janacek_works.models import Piece, Album


#classes for detail

class PieceDetailView(generic.DetailView):
    model = Piece
    template_name = 'database_of_janacek_works/piece_detail.html'

class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'database_of_janacek_works/album_detail.html'


def piece(request):
    return render_to_response('database_of_janacek_works/piece.html', {})

def album(request):
    return render_to_response('database_of_janacek_works/album.html', {})


class PieceJson(BaseDatatableView):

       # The model we're going to show
       model = Piece


       #define the columns that will be returned
       columns = ['piece_id', 'cz_title', 'en_title', 'jw_catalogue_number_part_I', 'time_of_composition', 'date_of_premiere',
                  'place_of_premiere', 'compose_for', 'number_of_movement', 'wiki']

       #define column names that will be used in sorting
       order_columns = ['piece_id', 'cz_title', 'en_title', 'jw_catalogue_number_part_I', 'time_of_composition', 'date_of_premiere',
                        'place_of_premiere', 'compose_for', 'number_of_movement', 'wiki']

       # set max limit of records returned, this is used to protect our site if someone tries to attack our site and make it return huge amount of data
       max_display_length = 300

       def render_column(self, row, column):
           # We want to render jw_catalogue_number as a custom column
            if column == 'jw_catalogue_number_part_I':
                return '{0} / {1}'.format(row.jw_catalogue_number_part_I, row.jw_catalogue_number_part_II)
            else:
                return super(PieceJson, self).render_column(row, column)


class AlbumJson(BaseDatatableView):

    model = Album

    columns = ['album_id', 'label_name', 'catalogue_number', 'album_name', 'album_published_year', 'published_country', 'number_of_media',
               'recording_technology', 'diameter', 'rpm', 'region_code', 'side_coumpling', 'tv_system', 'sound_system', 'medium_type', 'subtitles',
               'comment', 'text_language', 'text_by', 'note_language', 'note_by', 'libretto_language', 'libretto_by']

    order_columns = ['album_id', 'label_name', 'catalogue_number', 'album_name', 'album_published_year', 'published_country', 'number_of_media',
                     'recording_technology', 'diameter', 'rpm', 'region_code', 'side_coumpling', 'tv_system', 'sound_system', 'medium_type', 'subtitles',
                     'comment', 'text_language', 'text_by', 'note_language', 'note_by', 'libretto_language', 'libretto_by']

    max_display_length = 4000


