from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

    class Meta:
        db_table = 't_user'


class Emp(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.IntegerField()

    class Meta:
        db_table = 't_emp'
