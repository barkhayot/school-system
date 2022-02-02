from django.forms import ModelForm
from django import forms
from .models import ClassStudent, ClassStudentModel

class CourseEnrollForm(ModelForm):
    class Meta:
        model = ClassStudent
        fields = []

class CourseModelEnrollForm(ModelForm):
    class Meta:
        model = ClassStudentModel
        fields = []
