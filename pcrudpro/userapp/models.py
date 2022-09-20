from django.db import models

# Create your models here.
class Registraion(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    mobile = models.BigIntegerField(unique=True)
    address = models.TextField()
    pincode = models.BigIntegerField()
