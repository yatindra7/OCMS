from django.test import SimpleTestCase, TestCase
from users.forms import UserRegistrationForm, ProfileUpdateForm, UserUpdateForm


class Testforms(TestCase):

    def test_user_reg_form(self):
        form = UserRegistrationForm(data={
            'first name': 'srishty',
            'last_name': 'gandhi',
            'username': 'srishty11',
            'email': 'srishtygandhi@gmail.com',
            'password1': 'yatindra11',
            'password2': 'yatindra11'

        })

        self.assertTrue(form.is_valid())

    def test_profile_update_form(self):
        form = ProfileUpdateForm(data={
            'image': 'image.jpg'
        })
        self.assertTrue(form.is_valid())

    def test_user_update_form(self):
        form = UserUpdateForm(data={
            'first_name': 'yatindra',
            'last_name': 'indoria',
            'username': 'yatindra',
            'email': 'yatindraindoria75@gmail.com'
        })
        self.assertTrue(form.is_valid())
