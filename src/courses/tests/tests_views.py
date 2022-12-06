
from http import client
from pydoc import cli
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_update_course_GET(self):
        client = Client(self)
        response = client.get(reverse('courses:update_course', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_delete_course_GET(self):
        client = Client(self)
        response = client.get(reverse('courses:delete_course', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_course_list_get(self):
        client = Client(self)
        response = client.get(reverse('courses:course_list'))
        self.assertEquals(response.status_code, 200)

    def test_course_create_get(self):
        client = Client(self)
        response = client.get(reverse('courses:create_course'))
        self.assertEquals(response.status_code, 302)
