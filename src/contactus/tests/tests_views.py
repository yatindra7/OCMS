from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_contact_GET(self):
        client = Client(self)
        response = client.get(reverse('contactus:contact'))
        self.assertEquals(response.status_code, 200)
