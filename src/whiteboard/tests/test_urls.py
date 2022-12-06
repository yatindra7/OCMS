from django.test import SimpleTestCase
from django.urls import reverse, resolve
from whiteboard.views import live, whiteboard


class TestUrls(SimpleTestCase):
    def test_whiteboard_url_isresolved(self):
        url = reverse('whiteboard:whiteboard')
        self.assertEqual(resolve(url).func, whiteboard)

    def test_liveboard_url_isresolved(self):
        url = reverse('whiteboard:live')
        self.assertEqual(resolve(url).func, live)
