# Generated by Django 3.1.1 on 2020-09-13 17:28

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0003_employee_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='resume',
            field=ckeditor.fields.RichTextField(default='resume'),
            preserve_default=False,
        ),
    ]
