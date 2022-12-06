import imp
from django.test import TestCase
from comments.forms import PrivateCommentForm, CommentCreateForm


class Test_forms(TestCase):
    def test_create(self):
        form = CommentCreateForm(data={
            'comment_text': 'something'
        })

        self.assertTrue(form.is_valid())

    def test_private(self):
        form = PrivateCommentForm(data={
            'comment_text': 'something'
        })

        self.assertTrue(form.is_valid())
