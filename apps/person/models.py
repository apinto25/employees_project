from django.db import models

from apps.department.models import Department

from ckeditor.fields import RichTextField


class Skill(models.Model):
    skill = models.CharField('Skill', max_length=50)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Employee Skills'

    def __str__(self):
        return str(self.id) + '-' + self.skill


class Employee(models.Model):

    JOB_CHOICES = (
        ('0', 'Accountant'),
        ('1', 'Administrator'),
        ('2', 'Economist'),
        ('3', 'Other')
    )

    first_name = models.CharField('First name', max_length=60)
    last_name = models.CharField('Last name', max_length=60)
    full_name = models.CharField('Full name', max_length=60, blank=True)
    job = models.CharField('Job', max_length=50, choices=JOB_CHOICES)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    #avatar = models.ImageField(upload_to='employee', blank=True, null=True)
    skill = models.ManyToManyField(Skill)
    resume = RichTextField()

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees of the company"
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'department')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + ' ' + self.last_name
