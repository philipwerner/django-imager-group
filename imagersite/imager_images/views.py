"""Views module for imager_images."""
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, TemplateView
from django.contrib.auth.models import User
from imager_images.models import Album, ImagerProfile, Photo
from imager_images.forms import DocumentForm, AlbumForm


class AlbumView(ListView):
    """Display album for user."""

    model = Album
    context_object_name = 'albums'
    template_name = 'imager_images/album.html'

    def get_queryset(self):
        """Request users profile."""
        user = ImagerProfile.objects.get(user=self.request.user)
        return Album.objects.filter(user=user)
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
    user = ImagerProfile.objects.get(user=request.user)
    albums = Album.objects.filter(user=user).order_by('-date_uploaded')
    photos = Photo.objects.filter(user=user).order_by('-date_uploaded')
    return render(request, 'imager_images/library.html',
                  context={'photos': photos, 'albums': albums})


class PublicLibrary(TemplateView):
    """Display album for user."""
    template_name = 'imager_images/library.html'

    def get_context_data(self, **kwargs):
        """Request users profile."""
        # import pdb; pdb.set_trace()
        name = User.objects.get(username=kwargs['user'])
        user = ImagerProfile.objects.get(user=name)
        albums = Album.objects.filter(user=user)\
            .filter(published='PUBLIC').order_by('-date_uploaded')
        photos = Photo.objects.filter(user=user)\
            .filter(published='PUBLIC').order_by('-date_uploaded')
        context = super().get_context_data(**kwargs)
        context['photos'] = photos
        context['albums'] = albums
        return context


class PhotoListView(ListView):
    """Class to display the photo list view."""
    context_object_name = 'photos'
    template_name = 'imager_images/photo.html'

    def get_queryset(self):
        # profile = ImagerProfile.objects.get(user=self.request.user)
        # return Photo.objects.filter(user=profile)
        return Photo.objects.all().filter(published='PUBLIC').order_by('-date_uploaded')