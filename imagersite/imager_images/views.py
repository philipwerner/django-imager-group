from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile


# Create your views here.
class AlbumView(ListView):
    """Display album for user."""

    model = Album
    context_object_name = 'albums'
    template_name = 'imager_images/album.html'

    def get_queryset(self):
        """Request users profile."""
        # user = ImagerProfile.objects.get(user=self.request.user)
        # return Album.objects.filter(user=user)
        return Album.objects.all()


class AlbumPhotoView(DetailView):
    """Display album for user."""

    model = Album
    context_object_name = 'photo'
    template_name = 'imager_images/albumphoto.html'


    def get_context_data(self, **kwargs):
        photo = kwargs['object'].photo.filter(album=kwargs['object'].pk)
        context = super().get_context_data(**kwargs)
        context['photo'] = photo
        return context


def library_view(request):
    """Callable view for the libraaries."""
    photos = Photo.objects.all().filter(published='PUBLIC').order_by('-date_uploaded')
    return render(request, 'imager_images/library.html', context={'photos': photos})


class PhotoListView(ListView):
    """Class to display the photo list view."""
    context_object_name = 'photos'
    template_name = 'imager_images/photo.html'

    def get_queryset(self):
        return Photo.objects.all().filter(published='PUBLIC').order_by('-date_uploaded')