from django.test import TestCase
from contactus.forms import ContactUsForm


class Testing (TestCase):
    def test_form(self):
        forms = ContactUsForm(data={
            'email': 'srishtygandhi@gmail.com',
            'name': 'Srishty',
            'subject': 'idk',
            'message': 'something maybe'
        })

        self.assertTrue(forms.is_valid())
