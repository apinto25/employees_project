from django.db import models


class Department(models.Model):
    name = models.CharField('Name', max_length=50)
    short_name = models.CharField('Short name', max_length=20)

    def __str__(self):
        return str(self.id) + self.name
