from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_whiteboard_GET(self):
        client = Client(self)
        response = client.get(reverse('posts:create_post', args=[1]))

        self.assertEquals(response.status_code, 302)
