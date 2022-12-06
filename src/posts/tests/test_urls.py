#from multiprocessing.connection import Client
from urllib import request, response
from cv2 import ROTATE_90_COUNTERCLOCKWISE
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from classroom.models import Classroom
from posts.views import create_post
from posts.models import Post
from django.contrib.auth.models import User


# class TestUrls(SimpleTestCase):
#     def test_create_post_url_isresolved(self):
#         url = reverse('posts:create_post', args=[Classroom.pk])
#         self.assertEqual(resolve(url).func, create_post)

class TestUrls(TestCase):

    def test_turnin_url_isresolved(self):
        url = reverse('posts:create_post', args=[1])
        self.assertEqual(resolve(url).func, create_post)
