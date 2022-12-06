from django.test import TestCase, Client
from django.urls import reverse
import json
from .models import User,Profile
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm

# commented login_required

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user()
    def test_whiteboard_POST(self):
        response = self.client.post()
        