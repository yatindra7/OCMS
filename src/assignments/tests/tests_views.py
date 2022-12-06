from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_view_grades_GET(self):

        client = Client(self)
        response = client.get(reverse('assignments:view_grades', args=[1]))

        self.assertEquals(response.status_code, 302)

    def test_grade_GET(self):

        client = Client(self)
        response = client.get(reverse('assignments:grade', args=[1]))

        self.assertEquals(response.status_code, 302)
