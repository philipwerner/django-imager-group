"""Views for this awesome app."""
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.auth.models import User
from django.views.generic import TemplateView, CreateView
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile


class UserView(TemplateView):
    """View profile of other users."""

    model = ImagerProfile

    def get_context_data(self, username=None):
        """Get the context."""


class ProfileView(TemplateView):
    """Profile view class based view."""

    model = ImagerProfile

    # def get_context_data(self, username=None):
    #     """Get context data for view."""
    #     user = self.request.user.get(username=username)
    #     photo = Photo.objects.order_by('?').first()
    #     album = Album.objects.order_by('?').first()
    #     return {'photo': photo,
    #             'album': album,
    #             'user': user}


class EditProfileView(CreateView):
    """."""

    model = ImagerProfile
    fields = [
        'website',
        'location',
        'bio',
        'camera',
        'services',
        'photo_styles',
        'fee',
        'phone'
    ]
    success_url = reverse_lazy('user_profile')
    
    # def get_context_data(self, username=None):
    #     """Get context data for view."""
    #     user = User.objects.get(username=username)
    #     return {'user': user}
    def form_valid(self, form):
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
            self.object = form.save()
            return super(EditProfileView, self).form_valid(form)
        else:
            raise Http404()


class AddImage(CreateView):
    """View for adding a image."""

    model = Photo
    fields = [
        'image',
        'title',
        'description',
        'published'
    ]
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """."""
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            self.object = form.save()
            return super(AddImage, self).form_valid(form)
        else:
            raise Http404()


class AddAlbum(CreateView):
    """View for adding a album."""

    model = Album
    fields = [
        'cover',
        'title',
        'description',
        'published'
    ]
    success_url = reverse_lazy('library')

    def form_valid(self, form):
        """."""
        if self.request.user.is_authenticated:
            form.instance.user = self.request.user
            self.object = form.save()
            return super(AddAlbum, self).form_valid(form)
        else:
            raise Http404()
