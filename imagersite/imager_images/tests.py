from django.test import TestCase

import factory

from imager_images.models import Album, Photo

from imager_profile.models import ImagerProfile, User


class PhotoFactory(factory.django.DjangoModelFactory):
    """Factory for photos for testing"""

    class Meta:
        """Meta class"""

        model = Photo
    title = factory.Sequence(lambda n: f'Photo{n}')

class PhotoTestCase(TestCase):
    """Test case for the photos"""

    def setUp(self):
        """Setup"""
        larry = User(username='Larry', password='coolpassword')
        larry.save()
        l_profile = larry.profile
        l_profile.location = "Denver"
        l_profile.save()
        album = Album(user=l_profile, title='Denver City')
        album.save()
        for i in range(20):
            photo = PhotoFactory.build()
            photo.user = l_profile
            photo.save()
            album.photos.add(photo)
        self.album = album

    def test_has_20_photos(self):
        """Test for 20 photos for Larry"""
        first_user = User.objects.first()
        self.assertEqual(first_user.profile.photo_set.count(), 20)

    def test_album_is_created(self):
        """Test that album is created"""
        larry_album = Album.objects.get()
        self.assertIsNotNone(larry_album)
