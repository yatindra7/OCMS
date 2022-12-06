from django.test import TestCase, Client
from django.urls import reverse
import json

# commented login_required

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_whiteboard_GET(self):
        response = self.client.get(reverse('whiteboard:whiteboard'))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'whiteboard/whiteboard.html')

    def test_liveboard_GET(self):
        response = self.client.get(reverse('whiteboard:live'))
        print(response)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response,'whiteboard/liveboard.html')
