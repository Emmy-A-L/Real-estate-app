from django.db import models
from datetime import date

# Create your models here.

class listings(models.Model):

    CATEGORIES = [
        ('House For Sale', 'house for sale'),
        ('Land For Sale', 'land for sale'),
        ('House For Lease', 'house for lease'),
        ('Land For Lease', 'land for lease'),
    ]

    HOUSETYPES = [
        ('Apartment', 'apartment'),
        ('Bungalow', 'bungalow'),
        ('Duplex', 'duplex'),
        ('Flat', 'flat'),
        ('Terrace', 'terrace'),
    ]

    AVAILABILITY_CHOICES = [
        ('Available', 'available'),
        ('Not Available', 'not available'),
    ]

    title = models.CharField(max_length=200)
    available = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    description = models.TextField()
    location = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images/')
    upload_date = models.DateField(auto_now_add=date.today)

    if category == 'House For Sale' or category == 'House For Lease':
        house_type = models.CharField(max_length=50, choices=HOUSETYPES)
        
    elif category == 'Land For Sale' or category == 'Land For Lease':
        land_size = models.CharField(max_length=50)

    if available == 'Available':
        status = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES)
    
    def __str__(self):
        return self.title