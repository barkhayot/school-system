from django.urls import path
from . import views

urlpatterns = [
    path('getCourses/', views.GetCourses, name='GetCourses'),
    path('createCourse/', views.CourseCreate, name='CourseCreate'),
    path('errorPage/', views.errorPage, name='ErrorPage'),
    path('classwithprofID/', views.GetClassWithProfID, name='classwithprofID'),
    path('studentswithclassID/<int:pk>/', views.GetStudentsWithClassID, name='studentswithclassID'),
]