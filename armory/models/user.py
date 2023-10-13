from django.db import models

class User(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)
    username = models.CharField(max_length=120, blank=False, null=False, unique=True)
    email = models.EmailField(unique=True, blank=False, null=False)
    password = models.CharField(max_length=70, blank=False, null=False)
    telegram_token = models.CharField(max_length=120, unique=True)