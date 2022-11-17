from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50,default="")
    regno = models.CharField(max_length=50, primary_key=True)
    email = models.CharField(max_length=50, default="")
    phone = models.CharField(max_length=50, default="")
    year = models.CharField(max_length=50, default="")
    branch = models.CharField(max_length=50, default="")
    address = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.name