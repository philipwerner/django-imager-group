"""Test module for imagersite views."""
from django.test import Client, TestCase
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.core import mail
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

    def test_logging_in_with_nonexistent_user_goes_back_to_login_page(self):
        """Test login view has 200 status."""
        response = self.client.post(
            reverse_lazy('login'),
            {
                'username': 'chicken',
                'password': 'hatchtheeggs'
            }
        )
        html = soup(response.content, 'html.parser')
        error_item = html.find('ul', {'class': 'errorlist'}).find('li')
        self.assertTrue(
            error_item.text == 'Please enter a correct username and password. Note that both fields may be case-sensitive.')
        self.assertTemplateUsed(response, 'imagersite/login.html')

    def test_good_login_returns_user_to_homepage(self):
        """Test after good login, user returned to homepage."""
        user = User(username='awesomeuser', email='awesome@user.com')
        user.set_password('coolpassword')
        user.save()

        response = self.client.post(
            reverse_lazy('login'),
            {
                'username': user.username,
                'password': 'coolpassword'
            },
            follow=True
        )
        self.assertTemplateUsed(response, 'imagersite/home.html')
        self.assertContains(response, bytes(user.username, 'utf8'))

    def test_post_reg_goes_to_reg_complete(self):
        """Test after valid registration, user taken to reg complete page."""
        data = {
            'username': 'cooluser',
            'password1': 'awesomepassword',
            'password2': 'awesomepassword',
            'email': 'awesome@cool.com'
        }
        response = self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        self.assertContains(response, bytes(
            "Account has been registered, an email has been sent to your email to activate.", 'utf8'))

    def test_registered_user_exists_as_inactive(self):
        """Test valid reg creates user and sets them as inactive."""
        data = {
            'username': 'cooluser',
            'password1': 'awesomepassword',
            'password2': 'awesomepassword',
            'email': 'awesome@cool.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        self.assertTrue(User.objects.count() == 1)
        self.assertFalse(User.objects.first().is_active)

    def test_email_sent_on_valid_reg(self):
        """Test that activation email is sent on valid reg."""
        data = {
            'username': 'cooluser',
            'password1': 'awesomepassword',
            'password2': 'awesomepassword',
            'email': 'awesome@cool.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        # import pdb; pdb.set_trace()
        self.assertEqual(len(mail.outbox), 1)
        email = mail.outbox[0]
        self.assertEqual(email.subject, "imager registration email")
        content = mail.outbox[0].message().get_payload()
        self.assertTrue(content.startswith(
            '\n\nActivate account at testserver:\n\nhttp://testserver/accounts/activate/'))
        self.assertIn('awesome@cool.com', email.to)

    def test_activation_link_activates_account(self):
        """Test clicking activation link activates account."""
        data = {
            'username': 'cooluser',
            'password1': 'awesomepassword',
            'password2': 'awesomepassword',
            'email': 'awesome@cool.com'
        }
        self.client.post(
            reverse_lazy('registration_register'),
            data,
            follow=True
        )
        content = mail.outbox[0].message().get_payload()
        link = content.split('\n\n')[2]
        self.client.get(link)
        self.assertTrue(User.objects.count() == 1)
        user = User.objects.get(username='cooluser')
        self.assertTrue(user.is_active)
