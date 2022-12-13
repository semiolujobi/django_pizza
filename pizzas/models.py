from django.db import models
from django.contrib.auth.models import User
from django.views.generic import DetailView

class Pizza(models.Model):
    pizza_name = models.CharField(max_length=100)
    pizza_image = models.ImageField(null=True, blank=True, upload_to="images/")
    def __str__(self):
        return self.pizza_name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.TextField()
    def __str__(self):
        return self.topping_name
    
class Comment(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    comment = models.TextField()
    def __str__(self):
        return self.comment

class ImageDisplay(DetailView):
    model = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/')