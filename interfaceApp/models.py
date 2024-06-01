from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    order_message = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"
