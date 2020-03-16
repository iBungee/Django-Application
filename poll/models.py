from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Availability(models.Model):
    person = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    available = models.BooleanField()