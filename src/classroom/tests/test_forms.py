from django.test import TestCase
from classroom.forms import ClassroomCreationForm, AssignmentCreateForm, AssignmentFileForm, PostForm, JoinClassroomForm


class Test_forms(TestCase):
    def test_join_class(self):
        form = JoinClassroomForm(data={
            'code': 'dodo3'
        })
        self.assertTrue(form.is_valid())

    def test_class_create(self):
        form = ClassroomCreationForm(data={
            'name': 'physics',
            'description': 'ph class',
            'time_slot': 'every montay to friday 10 am'
        })
        self.assertTrue(form.is_valid())
