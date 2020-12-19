from django.contrib import admin
from django.urls import path

from apps.person import views

urlpatterns = [
    path('list-employees/', views.ListAllEmployees.as_view()),
    path('list-by-area/<short_name>', views.ListEmployeesByArea.as_view()),
]
