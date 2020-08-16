from django.db import models

from apps.department.models import Department


JOB_CHOICES = (
    ('0', 'Accountant'),
    ('1', 'Administrator'),
    ('2', 'Economist'),
    ('3', 'Other')
)

class Employee(models.Model):
    first_name = models.CharField('First name', max_length=60)
    last_name = models.CharField('Last name', max_length=60)
    job = models.CharField('Job', max_length=50, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    #image = models.ImageField(upload_to=None, height_field=None, width_field=None)

    def __str__(self):
        return str(self.id) + self.first_name + self.last_name
