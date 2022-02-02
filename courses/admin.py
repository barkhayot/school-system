from django.contrib import admin
from .models import Course, CourseModel
# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_number', 'professor', 'department', 
                    'description', 'credit', 'place')
    prepopulated_fields = {'slug': ('course_name',)}

class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'course_num', 'professor', 'department', 
                    'description', 'credit', 'place')

admin.site.register(CourseModel, CourseModelAdmin)

admin.site.register(Course, CourseAdmin)