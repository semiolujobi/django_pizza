from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    path('', views.index, name='index'),
    path('pizzanames', views.pizzanames, name='pizzanames'),
    path('pizzaname/<int:pizzaname_id>/', views.pizzaname, name='pizzaname'),
    path('comment/<int:pizzaname_id>/', views.comment, name='comment')
]   

