from django.db import models
from accounts.models import Account
from departments.models import Department
from django.core.validators import MaxValueValidator
from django.urls import reverse

# Create your models here.
class Course(models.Model):
    course_name     = models.CharField(max_length=255, unique=True)
    course_number   = models.PositiveIntegerField(primary_key=True, validators=[MaxValueValidator(9999999999)])
    professor       = models.ForeignKey(Account, on_delete=models.CASCADE)
    department      = models.ForeignKey(Department, on_delete=models.CASCADE)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=1000, blank=True)
    credit          = models.IntegerField()
    place           = models.IntegerField()
    enrolled        = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)

    def get_url(self):
        return reverse('course_detail', args=[self.department.slug, self.slug])

    def __str__(self):
        return self.course_name




class CourseModel(models.Model):
    course_name     = models.CharField(max_length=255, unique=True)
    course_num      = models.CharField(max_length=15, unique=True)
    professor       = models.ForeignKey(Account, on_delete=models.CASCADE)
    department      = models.ForeignKey(Department, on_delete=models.CASCADE)
    description     = models.TextField(max_length=1000, blank=True)
    credit          = models.IntegerField()
    place           = models.IntegerField()
    enrolled        = models.BooleanField(default=False)
    created_at      = models.DateTimeField(auto_now_add=True)

   

    def __str__(self):
        return self.course_name

