from django.db import models
from django.urls import reverse


# Create your models here.

class Department(models.Model):
    department_name     = models.CharField(max_length=255, unique=True)
    slug                = models.SlugField(max_length=100, unique=True)

    def get_url(self):
        return reverse('courses_by_departments', args=[self.slug])

    def __str__(self):
        return self.department_name