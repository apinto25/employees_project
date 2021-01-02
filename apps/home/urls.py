from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('test/', views.GenericTestView.as_view()),
    path('list/', views.ListTestListView.as_view()),
    path('list-test/', views.ListTest2ListView.as_view()),
    path('add/', views.CreateViewTestView.as_view(), name="test_add"),
]
