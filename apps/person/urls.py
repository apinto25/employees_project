from django.contrib import admin
from django.urls import path

from apps.person import views

urlpatterns = [
    path('list-employees/', views.ListAllEmployees.as_view()),
    path('list-by-area/<short_name>/', views.ListEmployeesByArea.as_view()),
    path('search-employee/', views.ListEmployeesByKword.as_view()),
    path('skills-employee/<pk>/', views.ListEmployeeSkills.as_view()),
    path('show-employee/<pk>/', views.EmployeeDetailView.as_view()),
    path('add-employee/', views.EmployeeCreateView.as_view()),
]
