from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)

from apps.person.models import Employee


class HomeView(TemplateView):
    """ Loads home template."""
    template_name = "home.html"


class ListAllEmployees(ListView):
    """List all employees of the company."""
    template_name = "person/list_all.html"
    paginate_by = 10
    ordering = "first_name"

    def get_queryset(self):
        keyword = self.request.GET.get("kword", "")
        queryset = Employee.objects.filter(
            full_name__icontains=keyword,
        )
        return queryset


class ListEmployeesAdmin(ListView):
    """List all employees of the company."""
    template_name = "person/list_all_admin.html"
    paginate_by = 10
    ordering = "id"
    model = Employee


class ListEmployeesByArea(ListView):
    """List all Employees from an area of the company."""
    template_name = "person/list_by_area.html"
    paginate_by = 10
    context_object_name = "employees"

    def get_queryset(self):

        area = self.kwargs["short_name"]
        queryset = Employee.objects.filter(
            department__short_name=area
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


class SuccessView(TemplateView):
    template_name = "person/success.html"


class EmployeeCreateView(CreateView):
    template_name = "person/add_employee.html"
    model = Employee
    fields = [
        "first_name",
        "last_name",
        "job",
        "department",
        "skill",
        "resume",
        "avatar"
    ]
    success_url = reverse_lazy("person_app:all_employees_admin")

    def form_valid(self, form):
        employee = form.save()
        employee.full_name = employee.first_name + " " + employee.last_name
        employee.save()
        return super(EmployeeCreateView, self).form_valid(form)


class EmployeeUpdateView(UpdateView):
    model = Employee
    template_name = "person/update.html"
    fields = [
        "first_name",
        "last_name",
        "job",
        "department",
        "skill",
    ]
    success_url = reverse_lazy("person_app:all_employees_admin")

    def post(self, request ,*args, **kwargs):
        self.object = self.get_object()
        return super().post(request ,*args, **kwargs)

    def form_valid(self, form):
        return super(EmployeeUpdateView, self).form_valid(form)


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = "person/delete.html"
    success_url = reverse_lazy("person_app:all_employees_admin")
