from django.urls import path
from .views import *
app_name = 'cartApp'

urlpatterns = [
    path("payment/", paymentview, name='payment'),
]