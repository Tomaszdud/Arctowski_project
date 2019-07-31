from django.db import models
from django.contrib.auth.models import User

STORAGE = (())


class Case(models.Model):
    case_id = models.CharField(max_length=20)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    length = models.IntegerField()
    width = models.IntegerField()
    hight = models.IntegerField()
    weight = models.DecimalField(max_digits=2, decimal_places=1)
    storage_conditions = models.CharField(choices=STORAGE)


class InCase(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=1)
    unit_of_measurement = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=11, decimal_places=2)
    sum_of_value = models.DecimalField(max_digits=13, decimal_places=2)
    case = models.ForeignKey(Case, on_delete=models.CASCADE)

