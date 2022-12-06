from http import client
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse

from whiteboard.views import whiteboard


class TestViews(TestCase):
    def test_whiteboard_GET(self):
        client = Client(self)
        response = client.get(reverse('whiteboard:whiteboard'))

        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response, 'whiteboard/whiteboard.html')

    def test_live_GET(self):
        client = Client(self)
        response = client.get(reverse('whiteboard:live'))

        self.assertEquals(response.status_code, 302)
        # self.assertTemplateUsed(response, 'whiteboard/liveboard.html')
