# Generated by Django 3.1.1 on 2021-02-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_employee_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='employee'),
        ),
    ]