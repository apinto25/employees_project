from django.contrib import admin
from django.urls import path

from apps.person import views


app_name = "person_app"


urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
         "list-employees/",
         views.ListAllEmployees.as_view(), 
         name="all_employees"
     ),
    path("list-by-area/<short_name>/", views.ListEmployeesByArea.as_view()),
    path("search-employee/", views.ListEmployeesByKword.as_view()),
    path("skills-employee/<pk>/", views.ListEmployeeSkills.as_view()),
    path(
         "show-employee/<pk>/",
         views.EmployeeDetailView.as_view(),
         name="employee_details"
     ),
    path("add-employee/", views.EmployeeCreateView.as_view()),
    path("success/", views.SuccessView.as_view(), name="success"),
    path("update-employee/<pk>/", views.EmployeeUpdateView.as_view(),
         name="update_employee"),
    path("delete-employee/<pk>/", views.EmployeeDeleteView.as_view(),
         name="delete_employee"),
]
