from django.shortcuts import render

from django.views.generic import TemplateView, ListView


class GenericTestView(TemplateView):
    template_name = 'home/home_test.html'


class ListTestListView(ListView):
    template_name = 'home/list.html'
    context_object_name = 'list_numbers'
    queryset = ['1', '10', '20', '30']
