"""Module for image forms."""
from django import forms
from datetime import datetime
from imager_images.models import Photo, Album


class DocumentForm(forms.ModelForm):
    """Class for the Photo and Album form."""

    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public')
    ]
    published = forms.ChoiceField(choices=PUBLISHED)


class PhotoForm(DocumentForm):
    """Class for the Photo Form."""

    class Meta:
        """."""

        model = Photo
        fields = ('docfile', 'title', 'description', 'published')

    docfile = forms.ImageField(label='Select File')


class AlbumForm(DocumentForm):
    """Class for Album Form."""

    class Meta:
        """."""

        model = Album
        fields = ('docfile', 'title', 'description', 'published')

    docfile = forms.ImageField(label='Select File')
