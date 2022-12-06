from users.models import Profile
from classroom.models import Classroom, ClassroomTeachers
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
#import sys
#sys.path.append('..')
# Create your models here.


class Search(models.Model):

    query = models.CharField(max_length=200)
    results = models.ManyToManyField(Profile, related_name='results')
    #classrooms = models.ManyToManyField(Classroom, related_name='classes')
    #users = models.ManyToManyField(Profile, related_name='users')
    # teachers = models.ManyToManyField(
    #    ClassroomTeachers, related_name='teachers')
    #students = models.ManyToManyField(User, related_name='students')
