from django.db import models


# Create your models here.

class School(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=50)
    depid = models.CharField(max_length=100)

    class Meta:
        db_table = 'school'


class Department(models.Model):
    dname = models.CharField(max_length=100)

    class Meta:
        db_table = 'department'



