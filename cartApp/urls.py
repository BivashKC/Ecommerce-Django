from django.urls import path
from .views import *
app_name = 'cartApp'

urlpatterns = [
    path('clothes_cart/',clothes_cartview, name='clothes_cart'),
    path('flag_cart/',flag_cartview, name='flag_cart'),
    path('utensils_cart/',utensils_cartview, name='utensils_cart'),
]