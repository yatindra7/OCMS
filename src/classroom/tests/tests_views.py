from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def test_home_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:home'))
        self.assertEquals(response.status_code, 302)

    def test_redir_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:redir'))

        self.assertEquals(response.status_code, 302)

    def test_create_class_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:create_classroom'))
        self.assertEquals(response.status_code, 302)

    def test_join_class_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:join_classroom'))
        self.assertEquals(response.status_code, 302)

    def test_open_classroom_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:open_classroom', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_delete_class_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:delete_classroom', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_class_members_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:members_classroom', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_stu_work_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:student_work', args=[1]))
        self.assertEquals(response.status_code, 404)

    def test_ass_create_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:assignment_create'))
        self.assertEquals(response.status_code, 302)

    def test_ass_submit_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:assignment_submit', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_turnin_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:turnin', args=[2]))
        self.assertEquals(response.status_code, 302)

    def test_unsubmit_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:unsubmit', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_unsub_f_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:unsubmit_file', args=[1]))
        self.assertEquals(response.status_code, 302)

    def test_todo_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:todo'))
        self.assertEquals(response.status_code, 302)

    def test_toreview_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:toreview'))
        self.assertEquals(response.status_code, 302)

    def test_cw_GET(self):
        client = Client(self)
        response = client.get(reverse('classroom:classwork', args=[1]))
        self.assertEquals(response.status_code, 302)
