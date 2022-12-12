from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzanames(request):
    pizzanames = Pizza.objects.order_by('pizza_name')
    context = {'all_pizzas':pizzanames}
    return render(request, 'pizzas/pizzanames.html', context)

def profile(request):
    profile = Profile.objects.filter(user=request.user)

def pizzaname(request, pizzaname_id):
    pizzanames = Pizza.objects.get(id=pizzaname_id)
    toppings = Topping.objects.filter(pizzaname=pizzaname)
    context = {'pizzaname':pizzaname, 'toppings':toppings}
    return render(request, 'pizzas/pizzanames.html', context)