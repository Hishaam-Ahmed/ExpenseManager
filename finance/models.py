from django.db import models
from django.contrib.auth.models import User


class ListName(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="listname", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Expense(models.Model):
    list_name = models.ForeignKey(ListName, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    cost = models.FloatField()
