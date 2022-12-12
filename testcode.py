import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Pizzeria.settings")

import django
django.setup()

from pizzas.models import *

pizzas = Pizza.objects.get(id=1)

print(pizzas)

toppings= Topping.objects.filter(pizzas)
#for p in pizzas:
#    print (p)

#p = pizza.objects.get(id=1)
#print(p)

#meatlover = Pizza.objects.get(id=1)

#Toppings = Topping.objects.filter(pizzas=meatlover)#.order_by(topping_name)
#for t in Toppings:
#    print(t)