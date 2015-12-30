from django.conf.urls import url, patterns
from . import views
from django.contrib.auth.decorators import login_required
from database_of_janacek_works.views import AlbumJson, PieceJson

urlpatterns = patterns('',


    #url(r'^$',views.IndexView.as_view(), name='index'),

    #url for piece/album detail
    url(r'^piece/detail/(?P<pk>\d+)/$', views.PieceDetailView.as_view(), name='piece_detail'),
    url(r'^album/detail/(?P<pk>\d+)/$', views.AlbumDetailView.as_view(), name='album_detail'),

    #
    url(r'^piece/$',views.piece, name='janacek/piece'),
    url(r'^album/$',views.album, name='janacek/album'),
    #url(r'^arrangement/$',views.arrangement, name='janacek/arrangement'),

    #showing data from database in JSON format
    url(r'^rest/album/$', AlbumJson.as_view(), name='rest_album'),
    url(r'^rest/piece/$',PieceJson.as_view(), name='rest_piece'),
   # url(r'^rest/arrangement/$',ArrangementListJson.as_view(), name='rest_arrangement'),
)
