from django.urls import path
from .views import *
app_name = 'userdata'

urlpatterns = [
    path("login/", loginview, name='login'),
    path("signup/", signupview, name='signup'),
]