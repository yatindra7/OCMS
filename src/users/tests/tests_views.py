from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_whiteboard_GET(self):
        client = Client(self)
        response = client.get(reverse('users:register'))

        self.assertEquals(response.status_code, 200)

    def test_live_GET(self):
        client = Client(self)
        response = client.get(reverse('users:profile'))

        self.assertEquals(response.status_code, 302)
