from django.test import TestCase
from matplotlib.pyplot import title
from courses.forms import CourseCreationForm, CourseUpdateForm


class Test_forms(TestCase):
    # def test_creation(self):
    #     form = CourseCreationForm(data={
    #         'title': 'courseone',
    #         'description': 'idk',
    #         'link': 'https://stackoverflow.com/questions/46695150/django-search-fields-in-multiple-models',
    #         # 'image': ''

    #         # dk how to test image in a form
    #     })

    #     self.assertTrue(form.is_valid())

    def test_update(self):
        form = CourseUpdateForm(data={
            'title': 'other title',
            'description': 'blabla',
            'link': 'https://stackoverflow.com/questions/46695150/django-search-fields-in-multiple-models',
            'image': 'image.png'
        })

        self.assertTrue(form.is_valid())
