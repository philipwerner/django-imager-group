"""."""

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from imager_profile import views
from imager_images.views import PhotoListView

urlpatterns = [
    url(r'^photos', PhotoListView.as_view(), name='photo'),
    url(r'^photos/(?P<number>\d+)', PhotoListView.as_view(), name='photo'),
    url(r'^album$', views.album.view, name='album'),
    url(r'^album/(?P<number>\d+)', views.album_view, name='album'),
    url(r'^library', views.library_view, name='library'),
]