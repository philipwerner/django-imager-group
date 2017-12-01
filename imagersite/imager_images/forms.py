"""Module for image forms."""
from django import forms
from datetime import datetime
from imager_images.models import Photo


class FormBase(forms.ModelForm):
    """Class for the Photo form"""
    title = forms.CharField(label='Title', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea)
    PUBLISHED = [
        ('PRIVATE', 'Private'),
        ('SHARED', 'Shared'),
        ('PUBLIC', 'Public')
    ]
    published = forms.ChoiceField(choices=PUBLISHED)

    class Meta:
        """Meta stuffs."""

        abstract = True


class PhotoForm(FormBase):
    """Class for the Album Form."""
    docfile = forms.ImageField(label='Select File')
