"""Model module for images."""
from django.db import models
from imager_profile import ImagerProfile


# Create your models here.
class ImageBase(models.Model):
    """Base class for phot and album use."""

    PRIVATE = 'Private'
    SHARED = 'Shared'
    PUBLIC = 'Public'

    PUBLISHED = (
        (PRIVATE, 'Private'),
        (SHARED, 'Shared'),
        (PUBLIC, 'Public')
    )
    user = models.ForeignKey(ImagerProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500, blank=True, null=True)
    date_modified = models.DateField(auto_now=True)
    date_published = models.DateField(blank=True, nill=True)
    published = models.CharField(choices=PUBLISHED, max_lenght=10)

    class Meta:
        """Meta abstract stuffs."""

        abstract = True


class Photo(ImageBase):
    """Individual photo model."""

    image = models.ImageField(upload_to='images')
    date_uploaded = models.DateField(editable=False, auto_now_add=True)


class Album(ImageBase):
    """Individual album model."""

    photos = models.ManyToManyField(Photo, related_name='albums')
    cover = models.ImageField(upload_to='images')
    date_created = models.DateField(editable=False, auto_now_add=True)
