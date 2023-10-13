from django.db import models

class Cabinet(models.Model):
    name = models.CharField(max_length=120, blank=False, null=False)