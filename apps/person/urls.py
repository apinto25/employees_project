from django.contrib import admin
from django.urls import path


def person_test(self):
    print("-------------test-------------")


urlpatterns = [
    path('person/', person_test),
]
