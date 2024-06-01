from django.urls import path
from .views import *
app_name = 'interfaceApp'

urlpatterns = [
    path("contact/", contactview, name='contact'),
    path("about/", aboutview, name='about'),
]