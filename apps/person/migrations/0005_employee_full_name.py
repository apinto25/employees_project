# Generated by Django 3.1.1 on 2020-12-31 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_employee_resume'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='full_name',
            field=models.CharField(blank=True, max_length=60, verbose_name='Full name'),
        ),
    ]
