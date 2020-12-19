from django.contrib import admin
from .models import Employee, Skill


admin.site.register(Skill)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'first_name',
        'last_name',
        'department',
        'job',
        'full_name',
    )

    def full_name(self, obj):
        return obj.first_name + ' ' + obj.last_name

    search_fields = ('first_name',)
    list_filter = ('department', 'job', 'skill')
    filter_horizontal = ('skill',)
