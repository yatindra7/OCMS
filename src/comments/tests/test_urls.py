import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from numpy import delete
from comments.views import create_comment, create_private_comment


class TestUrls(SimpleTestCase):

    def test_list_url_isresolved(self):
        url = reverse('comments:create_comment', args=[1])
        self.assertEqual(resolve(url).func, create_comment)

    def test_create_url_isresolved(self):

        url = reverse('comments:private_comment', args=[1])
        self.assertEqual(resolve(url).func, create_private_comment)
