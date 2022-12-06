from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, profile
from django.contrib.auth.views import LoginView, LogoutView


class TestUrls(SimpleTestCase):
    def test_register_url_isresolved(self):
        url = reverse('users:register')
        self.assertEqual(resolve(url).func, register)

    def test_profile_url_isresolved(self):
        url = reverse('users:profile')
        self.assertEqual(resolve(url).func, profile)


# done
