

from http import client
from pydoc import cli
from urllib import response
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_ide_GET(self):
        client = Client(self)
        response = client.get(reverse('ide:ide'))
        self.assertEquals(response.status_code, 200)
