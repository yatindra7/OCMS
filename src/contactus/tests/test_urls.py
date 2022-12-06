import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from numpy import delete
from contactus.views import contact


class TestUrls(SimpleTestCase):
    def test_list_url_isresolved(self):
        url = reverse('contactus:contact')
        self.assertEqual(resolve(url).func, contact)
