from ast import arg
import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from numpy import delete
from classroom.models import Classroom
from courses.models import Course
from courses.views import course_list, create_course, delete_course, update_course


class TestUrls(SimpleTestCase):
    def test_list_url_isresolved(self):
        url = reverse('courses:course_list')
        self.assertEqual(resolve(url).func, course_list)

    def test_create_url_isresolved(self):

        url = reverse('courses:create_course')
        self.assertEqual(resolve(url).func, create_course)

    def test_delete_url_isresolved(self):

        url = reverse('courses:delete_course', args=[1])
        self.assertEqual(resolve(url).func, delete_course)

    def test_update_url_isresolved(self):

        url = reverse('courses:update_course', args=[1])
        self.assertEqual(resolve(url).func, update_course)
