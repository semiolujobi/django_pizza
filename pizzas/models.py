from django.db import models
from django.contrib.auth.models import User


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza_name = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()
    def __str__(self):
        return self.topping_name

class Profile(models.Model):
    first_name = models.CharField(User, max_length=200)
    last_name = models.CharField(User, max_length=200)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    