from django.contrib import admin
from django.urls import path

from . import views


app_name = "department_app"

urlpatterns = [
    path('list-departments/',
    views.DepartmentListView.as_view(),
    name="list_department"
    ),
    path(
        'new-department/',
        views.RegisterNewDepartmentView.as_view(),
        name="new_department"
    ),
]
