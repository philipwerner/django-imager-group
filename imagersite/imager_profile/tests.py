"""Test module for imager."""
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User

    username = 'Test'
    email = 'test@test.com'


class ProfileTestCase(TestCase):
    """ProfileTestCase 1."""

    def setUp(self):
        """Setup user test."""
        self.user = UserFactory.create()
        self.user.set_password('secret')
        self.user.website = 'www.photo.com'
        self.user.location = 'Seattle, WA'
        self.user.fee = 300
        self.user.camera = 'Nikon'
        self.user.services = 'Babies'
        self.user.bio = 'fake action babies'
        self.user.phone = '123-456-7890'
        self.user.photo_style = 'fake'
        self.user.user = 'test'
        self.user.save()

    def test_user_username(self):
        """Test that username is Test."""
        assert self.user.username == 'Test'

    def test_user_email(self):
        """Test that email is test@test.com."""
        assert self.user.email == 'test@test.com'

    def test_user_website(self):
        """Test that user website is www.photo.com."""
        assert self.user.website == 'www.photo.com'

    def test_user_active(self):
        """Test that user is set to active."""
        assert self.user.is_active is True

    def test_user_location(self):
        """Test that user location is Seattle, WA."""
        assert self.user.location == 'Seattle, WA'

    def test_user_fee(self):
        """Test that user fee is 300."""
        assert self.user.fee == 300

    def test_user_camera(self):
        """Test that user prefers the best."""
        assert self.user.camera == 'Nikon'

    def test_user_services(self):
        """Test that user takes pics of babies dressed as flowers."""
        assert self.user.services == 'Babies'

    def test_user_bio(self):
        """Test that the user bio is what it is."""
        assert self.user.bio == 'fake action babies'

    def test_user_phone(self):
        """Test for the user phone number."""
        assert self.user.phone == '123-456-7890'
