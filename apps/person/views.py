from django.shortcuts import render
from django.views.generic import ListView

from apps.person.models import Employee


class ListAllEmployees(ListView):
    """List all employees of the company."""
    template_name = "person/list_all.html"
    paginate_by = 10
    ordering = "first_name"
    model = Employee


class ListEmployeesByArea(ListView):
    """List all Employees from an area of the company."""
    template_name = "person/list_by_area.html"

    def get_queryset(self):

        area = self.kwargs["short_name"]
        queryset = Employee.objects.filter(
            department__name=area
        )
        return queryset


class ListEmployeesByKword(ListView):
    """List employees by keyword from html template."""
    template_name = "person/list_by_kword.html"
    context_object_name = "employees"

    def get_queryset(self):
        keyword = self.request.GET.get("kword",)
        queryset = Employee.objects.filter(
            first_name = keyword
        )
        return queryset
