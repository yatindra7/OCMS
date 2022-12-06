
from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_comment_GET(self):
        client = Client(self)
        response = client.get(reverse('comments:create_comment', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_private_comment_GET(self):
        client = Client(self)
        response = client.get(reverse('comments:private_comment', args=[1]))
        self.assertEquals(response.status_code, 302)
