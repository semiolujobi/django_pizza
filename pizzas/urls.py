from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('pizzanames', views.pizzanames, name='pizzanames'),
    path('pizzanames/<int:pizzaname_id>/', views.pizzaname, name='pizzaname'),
]   

