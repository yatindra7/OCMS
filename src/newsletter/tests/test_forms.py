from django.test import TestCase
from newsletter.forms import SubscribeForm


class TestForms(TestCase):
    def test_subscribeform(self):
        form = SubscribeForm(data={
            'email': 'srishtygandhi@gmail.com'
        })
