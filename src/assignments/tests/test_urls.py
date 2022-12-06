import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from numpy import delete
from assignments.views import view_grades, grade


class TestUrls(SimpleTestCase):
    def test_home_url_isresolved(self):
        url = reverse('assignments:view_grades', args=[1])
        self.assertEqual(resolve(url).func, view_grades)

    def test_assignment_url_isresolved(self):
        url = reverse('assignments:grade', args=[1])
        self.assertEqual(resolve(url).func, grade)
