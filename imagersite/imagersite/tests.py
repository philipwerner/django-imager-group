"""Test module for imagersite views."""
from django.test import Client, TestCase, RequestFactory
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core import mail
from imager_profile.views import home_view
from bs4 import BeautifulSoup as soup


class ViewTestCase(TestCase):
    """View test case."""

    def setUp(self):
        """Set up."""
        self.client = Client()

    def test_main_view_status_code_is_200(self):
        """Test for a 200 status code."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_page_inherits(self):
        """Test homepage has proper content."""
        response = self.client.get(reverse_lazy('homepage'))
        self.assertContains(response, b'Imager Home Page.')

    def test_homepage_pulls_from_base_template(self):
        """Test homepage pulls from the base template."""
        response = self.client.get(reverse_lazy('homepage'))
        self.assertTemplateUsed(response, 'imagersite/base.html')

    def test_home_page_has_login_link(self):
        """Test for login link on homepage."""
        response = self.client.get(reverse_lazy('homepage'))
        html = soup(response.content, 'html.parser')
        link = html.find('a', {'href': '/login/'})
        self.assertIsNotNone(link)

    def test_login_view_status_code_is_200(self):
        """Test for a 200 status code."""
        response = self.client.get(reverse_lazy('login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view_status_302(self):
        """Test logout view returns status 302."""
        response = self.client.get(reverse_lazy('logout'))
        self.assertEqual(response.status_code, 302)

    def test_reg_view_status_200(self):
        """Test registration page has a status code 200."""
        response = self.client.get(reverse_lazy('registration_register'))
        self.assertEqual(response.status_code, 200)
