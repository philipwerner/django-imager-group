from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ImagerProfile(models.Model):
    """Creates an ImagerProfile class."""

    CAMERA_CHOICES = [
        ('NIKON', 'Nikon'),
        ('ERSATZ', 'Ersatz'),
        ('NOTREAL', 'Notreal'),
    ]

    SERVICES = [
        ('BABIES', 'Babies'),
        ('WEDDINGS', 'Weddings'),
        ('ACTION', 'Action'),
    ]

    STYLES = [
        ('BW', 'B&W'),
        ('NOTBW', 'Not B&W'),
        ('FAKE', 'Fake'),
    ]

    website = models.CharField(max_length=180, blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    fee = models.FloatField(max_length=20, blank=True, null=True)
    camera= models.CharField(max_length=50, choices=CAMERA_CHOICES,
        blank=True,
        null=True)
    services = models.CharField(max_length=50, choices=SERVICES,
        blank=True,
        null=True)
    bio = models.TextField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo_styles = models.CharField(max_length=50, choices=STYLES,
        blank=True,
        null=True)
    is_active = models.BooleanField(default=True)
    user = models.OneToOneField(User)

    def active(self):
        """Return active users."""
        return [user.username for user in User.objects.all() if user.is_active]
