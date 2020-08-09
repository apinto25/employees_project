from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('test/', views.GenericTestView.as_view()),
    path('list/', views.ListTestListView.as_view()),
]
