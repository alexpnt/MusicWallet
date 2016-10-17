from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^music/new$', views.music_new, name='music_new'),
    url(r'^music/(?P<pk>\d+)/edit$', views.music_edit, name='music_edit'),
    url(r'^music/(?P<pk>\d+)/delete$', views.music_delete, name='music_delete'),

    url(r'^user/new$', views.user_new, name='user_new'),
    url(r'^user/(?P<pk>\d+)/edit$', views.user_edit, name='user_edit'),
    url(r'^user/(?P<pk>\d+)/delete$', views.user_delete, name='user_delete'),
]
