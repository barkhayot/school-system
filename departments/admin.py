from django.contrib import admin
from .models import Department

# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('department_name',)}
    list_display = ('department_name', 'slug')

admin.site.register(Department, DepartmentAdmin)
