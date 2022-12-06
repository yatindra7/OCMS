import imp
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from numpy import delete
from classroom.views import *


class TestUrls(SimpleTestCase):
    def test_home_url_isresolved(self):
        url = reverse('classroom:home')
        self.assertEqual(resolve(url).func, home)

    def test_create_class_url_isresolved(self):
        url = reverse('classroom:create_classroom')
        self.assertEqual(resolve(url).func, create_classroom)

    def test_join_class_url_isresolved(self):
        url = reverse('classroom:join_classroom')
        self.assertEqual(resolve(url).func, join_classroom)

    def test_open_class_url_isresolved(self):
        url = reverse('classroom:open_classroom', args=[1])
        self.assertEqual(resolve(url).func, open_classroom)

    def test_delete_class_url_isresolved(self):
        url = reverse('classroom:delete_classroom', args=[1])
        self.assertEqual(resolve(url).func, delete_classroom)

    def test_member_url_isresolved(self):
        url = reverse('classroom:members_classroom', args=[1])
        self.assertEqual(resolve(url).func, members)

    def test_stu_work_url_isresolved(self):
        url = reverse('classroom:student_work', args=[1])
        self.assertEqual(resolve(url).func, student_work)

    def test_ass_create_url_isresolved(self):
        url = reverse('classroom:assignment_create')
        self.assertEqual(resolve(url).func, assignment_create)

    def test_ass_submit_url_isresolved(self):
        url = reverse('classroom:assignment_submit', args=[1])
        self.assertEqual(resolve(url).func, assignment_submit)

    def test_turnin_url_isresolved(self):
        url = reverse('classroom:turnin', args=[1])
        self.assertEqual(resolve(url).func, turnin)

    def test_unsubmit_url_isresolved(self):
        url = reverse('classroom:unsubmit', args=[1])
        self.assertEqual(resolve(url).func, unsubmit)

    def test_todo_url_isresolved(self):
        url = reverse('classroom:todo')
        self.assertEqual(resolve(url).func, todo)

    def test_toreview_url_isresolved(self):
        url = reverse('classroom:toreview')
        self.assertEqual(resolve(url).func, toreview)

    def test_classwork_url_isresolved(self):
        url = reverse('classroom:classwork', args=[1])
        self.assertEqual(resolve(url).func, classwork)
