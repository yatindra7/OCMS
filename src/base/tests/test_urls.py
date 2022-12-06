import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from numpy import delete
from base.views import lobby, room, getToken, createMember, getMember, deleteMember


class TestUrls(SimpleTestCase):
    def test_home_url_isresolved(self):
        url = reverse('base:lobby')
        self.assertEqual(resolve(url).func, lobby)

    def test_redir_url_isresolved(self):
        url = reverse('base:room')
        self.assertEqual(resolve(url).func, room)

    def test_create_class_url_isresolved(self):
        url = reverse('base:getToken')
        self.assertEqual(resolve(url).func, getToken)

    def test_join_class_url_isresolved(self):
        url = reverse('base:createMember')
        self.assertEqual(resolve(url).func, createMember)

    def test_open_class_url_isresolved(self):
        url = reverse('base:deleteMember')
        self.assertEqual(resolve(url).func, deleteMember)

    def test_delete_class_url_isresolved(self):
        url = reverse('base:getMember')
        self.assertEqual(resolve(url).func, getMember)
