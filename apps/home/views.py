from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView

from .models import HomeTestModel


class GenericTestView(TemplateView):
    template_name = 'home/home_test.html'


class ListTestListView(ListView):
    template_name = 'home/list.html'
    context_object_name = 'list_numbers'
    queryset = ['1', '10', '20', '30']


class ListTest2ListView(ListView):
    template_name = 'home/list_test.html'
    model = HomeTestModel
    context_object_name = 'list'


class CreateViewTestView(CreateView):
    template_name = 'home/add.html'
    model = HomeTestModel
    fields = ['title', 'subtitle', 'quantity']
