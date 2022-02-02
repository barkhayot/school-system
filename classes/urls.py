from django.urls import path
from . import views

urlpatterns = [
    

    #test view

    path('enrolledCourseModel/', views.EnrolledCourseModel, name='enrolledCourseModel'),
    path('getCourseModel/', views.GetCourseModels, name='getCourseModel'),
    path('enrollCourseModel/<int:pk>/', views.EnrollCourseModel, name='enrollCourseModel'),
    path('getCourseModelError/<int:pk>', views.GetCourseModelError, name='getCourseModelError'),
    path('deleteCourseModel/<int:pk>/', views.DeleteCourseModel, name='deleteCourseModel'),
    path('courseModelDetail/<int:pk>', views.CourseModelDetail, name='courseModelDetail'),


]