from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, max_length=254)
    phonenumber = models.CharField(blank=True, max_length=15)

    USERNAME_FIELD = 'email' # by default in django ,when a user login it needs username + password , we are chaging it to email ,so when a user login now it needs email + passowrd
    REQUIRED_FIELDS = ['username'] # this is for creatsuperuser when you run this then it asks for username_field + password and then it will check if any other required_fields are there if yes then you have to fill that