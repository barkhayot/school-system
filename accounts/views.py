from django.shortcuts import render, redirect
from .models import Account
from .forms import StudentRegisterForm, ProfessorRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.models import CourseModel
from classes.models import ClassStudentModel





# Create your views here.

# Student Account Register View
def StudentRegister(request):

    if request.user.is_authenticated:
        return redirect('userPage')

    form = StudentRegisterForm()
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            account_id = form.cleaned_data['account_id']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user( account_id = account_id, first_name = first_name, last_name = last_name, email = email, username = username, password = password)
            user.phone_number = phone_number
            user.save()

            return redirect('accountLogin')

    context = {
        'form' : form
    }
    return render(request, 'accounts/studentRegister.html', context)

# Professor Account Register View
def ProfessorRegister(request):

    if request.user.is_authenticated:
        return redirect('userPage')

    form = ProfessorRegisterForm()
    if request.method == 'POST':
        form = ProfessorRegisterForm(request.POST)
        if form.is_valid():
            account_id = form.cleaned_data['account_id']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_professor( account_id = account_id, first_name = first_name, last_name = last_name, email = email, username = username, password = password)
            user.phone_number = phone_number
            user.save()

            return redirect('accountLogin')

    context = {
        'form' : form
    }
    return render(request, 'accounts/professorRegister.html', context)


# Account Login View
def AccountLogin(request):

    if request.user.is_authenticated:
        return redirect('userPage')
    if request.method == 'POST':
        email = request.POST['email']
        account_id = request.POST['account_id']
        password = request.POST['password'] 

        user = authenticate(request, email=email, account_id=account_id, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_professor:
                return redirect('professorPage')                
            return redirect('userPage')
        else:
            messages.info(request, 'Username or Password is incorrect')

    
    return render(request, 'accounts/accountLogin.html')

# User LogOut Page View
@login_required(login_url='accountLogin')
def AccountLogout(request):
    logout(request)
    return redirect('accountLogin')



# User Page View
@login_required(login_url='accountLogin')
def UserPage(request):
    user = request.user
    course = ClassStudentModel.objects.filter(student=request.user)

    context = {
        'users' : user,
        'courses' : course
    }
    return render(request, 'accounts/userPage.html', context)


@login_required(login_url='accountLogin')
def ProffessorPage(request):
    user = request.user
    course = CourseModel.objects.filter(professor=request.user)
    context = {
        'users' : user,
        'courses' : course
    }
    return render(request, 'accounts/professor/professorPage.html', context)


