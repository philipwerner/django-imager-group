"""Imager Profile model."""
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class ActiveManager(models.Manager):
    """Active subclass."""

    def get_queryset(self):
        """Query for subclass."""
        return super(ActiveManager, self).get_queryset().filter(user__is_active=True)


class ImagerProfile(models.Model):
    """Creates an ImagerProfile class."""

    CAMERA_CHOICES = [
        ('NIKON', 'Nikon'),
        ('ERSATZ', 'Ersatz'),
        ('NOTREAL', 'Notreal'),
        ('MINOLTA', 'Minolta'),
        ('CANNON', 'Cannon'),
        ('SONY', 'Sony')
    ]

    SERVICES = [
        ('BABIES', 'Babies'),
        ('WEDDINGS', 'Weddings'),
        ('ACTION', 'Action'),
        ('NATURE', 'Nature'),
        ('PORTRAIT', 'Portrait'),
        ('OTHER', 'Other'),
    ]

    STYLES = [
        ('BW', 'B&W'),
        ('COLOR', 'Color'),
        ('FAKE', 'Fake'),
    ]

    objects = models.Manager()
    active = ActiveManager()
    website = models.CharField(max_length=180, blank=True, null=True)
    location = models.CharField(max_length=180, blank=True, null=True)
    fee = models.FloatField(max_length=20, blank=True, null=True)
    camera = models.CharField(
        max_length=100,
        choices=CAMERA_CHOICES,
        blank=True,
        null=True
    )
    services = models.CharField(
        max_length=100,
        choices=SERVICES,
        blank=True,
        null=True
    )
    bio = models.TextField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    photo_styles = models.CharField(
        max_length=100,
        choices=STYLES,
        blank=True,
        null=True
    )
    active = models.BooleanField(default=True)
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)

    def __str__(self):
        """Function to print username."""
        return self.user.username

    @property
    def is_active(self):
        """Return active users."""
        return self.user.is_active


@receiver(post_save, sender=User)
def create_profile(sender, **kwargs):
    """Attach a profile after new user is created."""
    if kwargs['created']:
        profile = ImagerProfile(user=kwargs['instance'])
        profile.save()
