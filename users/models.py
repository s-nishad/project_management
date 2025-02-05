from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
