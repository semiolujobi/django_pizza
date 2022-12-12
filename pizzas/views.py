from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.http import Http404
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

def pizzanames(request):
    pizzanames = Pizza.objects.order_by('pizza_name')
    context = {'all_pizzas':pizzanames}
    return render(request, 'pizzas/pizzanames.html', context)

def pizzaname(request, pizzaname_id):
    p = Pizza.objects.get(id=pizzaname_id)
    toppings = Topping.objects.filter(pizza=p)
    comments = Comment.objects.filter(pizza=p)
    context = {'pizzaname':p, 'toppings':toppings,'comments':comments}
    return render(request, 'pizzas/pizzaname.html', context)

def comment(request, pizzaname_id):
    pizza = Pizza.objects.get(id=pizzaname_id)
    if request.method != "POST":
        form = CommentForm()
    else:
        print(request.POST)
        form = CommentForm(data=request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.pizza = pizza
            comment.save()
            return redirect('pizzas:pizzaname', pizzaname_id=pizzaname_id)
    context = {'form':form, 'pizza':pizza}
    return render(request, "pizzas/comment.html", context)