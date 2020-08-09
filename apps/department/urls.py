from django.contrib import admin
from django.urls import path


def department_test(self):
    print("-------------test-------------")


urlpatterns = [
    path('department/', department_test),
]
