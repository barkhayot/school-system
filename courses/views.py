from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, CourseModel
from .forms import CourseCreateForm
from classes.models import ClassStudentModel
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.auth.decorators import login_required



# Create your views here.

# All Courses View
@login_required(login_url='accountLogin')
def GetCourses(request):
    course = CourseModel.objects.all()
    
    context = {
        'courses' : course
    }
    return render(request, 'courses/courses.html', context)

# Course Create View
@login_required(login_url='accountLogin')
def CourseCreate(request):
    if request.user.is_professor:
        form = CourseCreateForm()
        if request.method == 'POST':
            form = CourseCreateForm(request.POST)
            if form.is_valid():
                course = form.save(commit=False)
                course.professor = request.user
                course.save()
                return redirect('professorPage')
    else:
         return redirect('ErrorPage')        

    context = {
        'form' : form
    }
    return render(request, 'courses/createCourse.html', context)


# Classes with prof ID
@login_required(login_url='accountLogin')
def GetClassWithProfID(request):
    class_pr = ClassStudentModel.objects.filter(couese__professor=request.user)

    context = {
        'class_prs' : class_pr
    }
    return render(request, 'courses/classeswithprofID.html', context)


# Students with Class ID
@login_required(login_url='accountLogin')
def GetStudentsWithClassID(request, pk):
    st_class = get_object_or_404(ClassStudentModel, pk=pk)
    st = ClassStudentModel.objects.filter(couese__professor=request.user)
    
    context = {
        'st_class' : st_class,
        'sts' : st
    }

    return render(request, 'courses/studentswithclassID.html', context)


# Error Handler View
@login_required(login_url='accountLogin')
def errorPage(request):
    return render(request, 'courses/errorPage.html')

