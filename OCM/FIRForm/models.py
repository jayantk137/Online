from django.db import models
from django.utils import timezone

# Create your models here.
class FIR(models.Model):
    STATUS_CHOICES = (
        ('Completed', 'Completed'),
        ('Not Updated', 'Not updated'),
        )
    city = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    zip = models.PositiveIntegerField()
    PoliceStation = models.CharField(max_length=64)
    VicFN = models.CharField(max_length=64)
    VicLN = models.CharField(max_length=64)
    ComplaintType = models.CharField(max_length=64)
    Description = models.TextField()
    ComFN = models.CharField(max_length=64)
    ComLN = models.CharField(max_length=64)
    publish = models.DateTimeField(default=timezone.now)
    Email = models.EmailField(max_length=254)
    status = status = models.CharField(max_length=15,choices=STATUS_CHOICES,default='Not Updated')