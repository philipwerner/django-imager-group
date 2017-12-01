"""Imager Images urls."""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from imager_profile import views
from imager_images.views import PhotoListView, AlbumView, AlbumPhotoView

app_name = 'imager_images'
urlpatterns = [
    url(r'^album$', AlbumView.as_view(), name='album'),
    url(r'^album/(?P<pk>\d+)', AlbumPhotoView.as_view(), name='albumphoto'),
    url(r'^photos', PhotoListView.as_view(), name='photo'),
    # url(r'^library', views.library_view, name='library'),
]
