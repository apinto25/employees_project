from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('new-department/', views.RegisterNewDepartmentView.as_view(), name="new_department"),
]
