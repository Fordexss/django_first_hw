from django.db import models


# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    description = models.TextField()
