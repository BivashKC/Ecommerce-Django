from django.urls import path
from .views import *
app_name = 'shopApp'

urlpatterns = [
    path("clothes/", clothesview, name='clothes'),
    path("flags/", flagview, name='flags'),
    path("utensils/", utensilsview, name='utensils'),
]