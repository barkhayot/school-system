from django.db import models
from accounts.models import Account
from courses.models import Course, CourseModel

# Create your models here.

class StudnetClass(models.Model):
    student     = models.ForeignKey(Account, on_delete=models.CASCADE)
    course      = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username



class ClassStudent(models.Model):
    student     = models.ForeignKey(Account, on_delete=models.CASCADE)
    course      = models.OneToOneField(Course, unique=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username


class ClassStudentModel(models.Model):
    student     = models.ForeignKey(Account, on_delete=models.CASCADE)
    couese      = models.ForeignKey(CourseModel, related_name='ClassStudentModel', on_delete=models.CASCADE)

    def __str__(self):
        return self.student.username

