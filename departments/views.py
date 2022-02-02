from django.shortcuts import render, redirect, get_object_or_404
from .models import Department
from django.contrib.auth.decorators import login_required
from courses.models import CourseModel

# Get Departments View
@login_required(login_url='accountLogin')
def GetDepartment(request):
    department = Department.objects.all()
    context = {
        'departments': department
    }
    return render(request, 'departments/getDepartments.html', context )

# Department Detail View
@login_required(login_url='accountLogin')
def DepartmentDetail(request, pk):
    department = get_object_or_404(Department, pk=pk)
    course = CourseModel.objects.filter(department=department)
    
    context = {
        'department' : department,
        'courses' : course
    }
    return render(request, 'departments/departmentDetail.html', context)
