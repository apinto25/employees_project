from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from apps.person.models import Employee
from apps.department.models import Department

from .forms import NewDepartmentForm


class RegisterNewDepartmentView(FormView):
    template_name = "department/new_department.html"
    form_class = NewDepartmentForm
    success_url = "/"

    def form_valid(self, form):


        dept = Department(
            name=form.cleaned_data["department"],
            short_name=form.cleaned_data["short_name"]
        )
        dept.save()

        name = form.cleaned_data["name"]
        last_name = form.cleaned_data["last_name"]

        Employee.objects.create(
            first_name=name,
            last_name=last_name,
            job=1,
            department=dept,
        )

        return super(RegisterNewDepartmentView, self).form_valid(form)
