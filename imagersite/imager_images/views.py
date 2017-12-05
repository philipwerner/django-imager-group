"""Views module for imager_images."""
from django.views.generic import TemplateView, ListView
from imager_images.models import Album, Photo


class LibraryView(TemplateView):
    """Library view class based view."""


class PhotoView(ListView):
    """Photo view class based view."""

    model = Photo

    def get_context_data(self, pk=None):
        """Get context data for view."""
        photo = Photo.objects.get(id=pk)
        return {'photo': photo}


class AlbumView(ListView):
    """Album view class based view."""

    model = Album

    def get_context_data(self, pk=None):
        """Get context data for view."""
        album = Album.objects.get(id=pk)
        return {'album': album}
