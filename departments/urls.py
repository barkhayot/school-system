from django.urls import path
from . import views

urlpatterns = [
    path('getDepartments/', views.GetDepartment, name='getDepartments'),
    path('departmentDetail/<int:pk>/', views.DepartmentDetail, name='departmentDetail'),
]