from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Clothes(models.Model):
    c_name = models.CharField(max_length=200)
    c_image = models.ImageField(upload_to='shopApp/clothes')
    c_desc = models.TextField(null=False, blank=False)
    c_price = models.IntegerField()
    c_original_price = models.IntegerField(default=5000)

    def __str__(self):
        return self.c_name
      
class Flags(models.Model):
    f_name = models.CharField(max_length=200)
    f_image = models.ImageField(upload_to='shopApp/flags')
    f_desc = models.TextField(null=False, blank=False)
    f_price = models.IntegerField()
    f_original_price = models.IntegerField(default=5000)

    def __str__(self):
        return self.f_name
    
class Utensils(models.Model):
    u_name = models.CharField(max_length=200)
    u_image = models.ImageField(upload_to='shopApp/utensils')
    u_desc = models.TextField(null=False, blank=False)
    u_price = models.IntegerField()
    u_original_price = models.IntegerField(default=5000)

    def __str__(self):
        return self.u_name