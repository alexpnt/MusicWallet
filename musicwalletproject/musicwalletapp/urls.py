from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #musics
    url(r'^music/new$', views.music_new, name='music_new'),
    url(r'^music/(?P<pk>\d+)/edit$', views.music_edit, name='music_edit'),
    url(r'^music/(?P<pk>\d+)/delete$', views.music_delete, name='music_delete'),
    #users
    url(r'^user/new$', views.user_new, name='user_new'),
    url(r'^user/(?P<pk>\d+)/edit$', views.user_edit, name='user_edit'),
    url(r'^user/(?P<pk>\d+)/delete$', views.user_delete, name='user_delete'),

    #rest api
    url(r'^api/users$', views.api_users,name='api_users'),
    url(r'^api/user/(?P<pk>\d+)$', views.api_user_details,name='api_user_details'),
    url(r'^api/user/new$', views.api_user_new,name='api_user_new'),
    url(r'^api/user/(?P<pk>\d+)/edit$', views.api_user_edit,name='api_user_edit'),
    url(r'^api/user/(?P<pk>\d+)/delete$', views.api_user_delete,name='api_music_user'),
    url(r'^api/musics$', views.api_musics,name='api_musics'),
    url(r'^api/music/(?P<pk>\d+)$', views.api_music_details,name='api_music_details'),
    url(r'^api/music/new$', views.api_music_new,name='api_music_new'),
    url(r'^api/music/(?P<pk>\d+)/edit$', views.api_music_edit,name='api_music_edit'),
    url(r'^api/music/(?P<pk>\d+)/delete$', views.api_music_delete,name='api_music_delete'),
    url(r'^api/music/(?P<pk1>\d+)/user/(?P<pk2>\d+)$', views.api_favourite_music,name='api_favourite_music'),
    

]

urlpatterns = format_suffix_patterns(urlpatterns)