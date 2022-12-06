import imp
from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from newsletter.views import subscribe

# class TestUrls(SimpleTestCase):
#     def test_subscribe_post_url_isresolved(self):
#         url = reverse('newsletter:subscribe')
#         self.assertEqual(resolve(url).func, subscribe)

# redirect issues


class TestUrls(TestCase):
    def test_subscribe_url_isresolved(self):
        url = reverse('newsletter:subscribe')
        self.assertEqual(resolve(url).func, subscribe)
