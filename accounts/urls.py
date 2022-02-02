from django.urls import path
from . import views

urlpatterns = [
    path('studentRegister/', views.StudentRegister, name='studentRegister'),
    path('professorRegister/', views.ProfessorRegister, name='professorRegister'),
    path('accountLogin/', views.AccountLogin, name='accountLogin'),
    path('accountLogout/', views.AccountLogout, name='accountLogout'),
    path('userPage/', views.UserPage, name='userPage'),
    path('professorPage/', views.ProffessorPage, name='professorPage'),
]