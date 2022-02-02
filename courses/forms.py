from django import forms
from django.forms import ModelForm
from .models import CourseModel
from django.core.exceptions import ValidationError



class CourseCreateForm(ModelForm):

    
    place = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Students'
    }))

    credit = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Credits'
    }))

    def clean_course_name(self):
        course_name = self.cleaned_data['course_name']
        if CourseModel.objects.filter(course_name=course_name).exists():
            raise ValidationError("Email already exists")
        return course_name

    
    class Meta:
        model = CourseModel
        fields = ['course_name', 'course_num', 'department', 
                    'description', 'credit', 'place']


    def __init__(self, *args, **kwargs):
        super(CourseCreateForm, self).__init__(*args, **kwargs)
        self.fields['course_name'].widget.attrs['placeholder']='Name of Course'
        self.fields['course_num'].widget.attrs['placeholder']='Course ID number'
        self.fields['department'].widget.attrs['placeholder']='Choose Department'
        self.fields['credit'].widget.attrs['placeholder']='Credits'
        self.fields['place'].widget.attrs['placeholder']='Students'
        self.fields['description'].widget.attrs['placeholder']='Description'
        
        for field in self.fields:
            self.fields[field].widget.attrs['class']='form-control'
