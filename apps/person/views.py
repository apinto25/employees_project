from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

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


class ListEmployeeSkills(ListView):
    """List skills by employee from html template."""
    template_name = "person/list_skills.html"
    context_object_name = "skills"

    def get_queryset(self):
        employee_id = self.kwargs["pk"]
        if Employee.objects.filter(id=employee_id).exists():
            employee = Employee.objects.get(id=employee_id)
            return employee.skill.all()
        else:
            return []


class EmployeeDetailView(DetailView):
    """Detail view of employee model from html template."""
    model = Employee
    template_name = "person/detail_employee.html"

    def get_context_data(self, **kwargs):
        context = super(EmployeeDetailView, self).get_context_data(**kwargs)
        context["title"] = "Employee of the month" 
        return context


class EmployeeCreateView(CreateView):
    template_name = "person/add_employee.html"
    model = Employee
    fields = ("__all__")
    success_url = "."
