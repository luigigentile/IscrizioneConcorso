from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    ruolo =  models.CharField(max_length=50,null=True) 
    telefono =  models.CharField(max_length=50,null=True)
    fax =  models.CharField(max_length=50,null=True)
