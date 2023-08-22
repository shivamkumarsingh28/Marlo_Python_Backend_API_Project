from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MarloUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class MarloProduct(models.Model):
    name = models.CharField(max_length=50)
    barcode = models.IntegerField()
    brand = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    available = models.CharField(max_length=10)

    def __str__(self):
        return self.name
