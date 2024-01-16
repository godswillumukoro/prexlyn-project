from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    PROPERTY_CHOICES = [
        ('house', 'house'),
        ('land', 'land'),
        ('apartment', 'apartment'),
        ('bungalow', 'bungalow'),
        ('duplex', 'duplex'),
        ('cottage', 'cottage'),
    ]

    property_choice = models.CharField(
        max_length=20,
        choices=PROPERTY_CHOICES,
        default='house',
    )

    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%d/%m/%Y/')
    photo_1 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_7 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_8 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_9 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_10 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_11 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_12 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_13 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_14 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    photo_15 = models.ImageField(upload_to='photos/%d/%m/%Y/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
