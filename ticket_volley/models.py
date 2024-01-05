from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True, null=True)

class Stadium(models.Model):
    name = models.CharField(max_length=100)

class Match(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    date = models.DateTimeField()

class Seat(models.Model):
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=10)
    is_available = models.BooleanField(default=True)
