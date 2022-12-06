from django.test import SimpleTestCase
from django.urls import reverse, resolve
from classroom.models import Classroom
from ide.views import problems, ide


class TestUrls(SimpleTestCase):
    def test_ide_url_isresolved(self):
        url = reverse('ide:ide')
        self.assertEqual(resolve(url).func, ide)

    def test_problems_url_isresolved(self):
        url = reverse('ide:problems')
        self.assertEqual(resolve(url).func, problems)
