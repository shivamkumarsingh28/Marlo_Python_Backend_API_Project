from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MarloUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username
