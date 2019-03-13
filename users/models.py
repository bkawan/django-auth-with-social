from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )
    telephone = models.CharField(max_length=20)
    zip = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True)
    oranges = models.DecimalField(decimal_places=2, max_digits=9, null=True, blank=True)
    active = models.BooleanField(default=False)
