from django.shortcuts import render, redirect, get_object_or_404
from courses.models import Course, CourseModel 
from .forms import CourseEnrollForm, CourseModelEnrollForm
from .models import StudnetClass, ClassStudent, ClassStudentModel
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


# Create your views here.

# Test View

# Enrolled Courses View
@login_required(login_url='accountLogin')
def EnrolledCourseModel(request):
    if request.user.is_professor:
        return redirect('professorPage') 
    course = ClassStudentModel.objects.filter(student=request.user)

    context = {
        'courses' : course
    }
    return render(request, 'classes/test/enrolledCourses.html', context)

# Get All Courses from CourseModel
@login_required(login_url='accountLogin')
def GetCourseModels(request):
    if request.user.is_professor:
        return redirect('professorPage') 

    course = CourseModel.objects.filter(enrolled=False)
    form = CourseEnrollForm()
    
    if request.method == 'POST':
        form = CourseModelEnrollForm(request.POST)
        if form.is_valid():
            st_class = form.save(commit=False)
            st_class.student = request.user
            st_class.couese = course
            try:
                st_class.save()
            except IntegrityError:
                return redirect('getCourseModelError', pk=course.id)
            return redirect('index')
    context = {
        'form':form,
        'courses' : course
    }
    return render(request, 'classes/test/getCourses.html', context)


# Enroll CourseModel By ID
@login_required(login_url='accountLogin')
def EnrollCourseModel(request, pk):
    if request.user.is_professor:
        return redirect('professorPage') 

    course = get_object_or_404(CourseModel, pk=pk)
    form = CourseModelEnrollForm()
    if request.method == 'POST':
        form = CourseModelEnrollForm(request.POST)
        if form.is_valid():
            st_class = form.save(commit=False)
            st_class.student = request.user
            st_class.couese = course
            try:
                st_class.save()
            except IntegrityError:
                return redirect('getCourseModelError', pk=course.id)
            return redirect('enrolledCourseModel')
    context = {
        'course': course,
        'form': form
    }
    return render(request, 'classes/test/testView.html', context)


# Get CourseModel Error View
@login_required(login_url='accountLogin')
def GetCourseModelError(request, pk):

    if request.user.is_professor:
        return redirect('professorPage') 

    course = get_object_or_404(CourseModel, pk=pk)
    
    context = {
        'course' : course
    }
    
    return render(request, 'classes/test/getCourseError.html', context)


# Course Detail View
@login_required(login_url='accountLogin')
def CourseModelDetail(request, pk):
    if request.user.is_professor:
        return redirect('professorPage') 

    course = get_object_or_404(ClassStudentModel, pk=pk)
    
    context = {
        'course' : course
    }

    return render(request, 'classes/test/courseDetail.html', context)



# Delete Course Model from the List View
@login_required(login_url='accountLogin')
def DeleteCourseModel(request, pk):
    if request.user.is_professor:
        return redirect('professorPage') 
        
    course = get_object_or_404(ClassStudentModel, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('enrolledCourseModel')
    context = {
        'course': course
    }
    return render(request, 'classes/test/deleteCourse.html', context)