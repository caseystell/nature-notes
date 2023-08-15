from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Amenity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('amenities_detail', kwargs={'pk': self.id})


class Campsite(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    amenities = models.ManyToManyField(Amenity)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'campsite_id': self.id})
    

class Trail(models.Model):
    name = models.CharField(max_length=100)
    length = models.CharField(max_length=50)
    campsite = models.ForeignKey(Campsite, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_trail_display()} @ {self.campsite}'


class Photo(models.Model):
    url = models.CharField(max_length=200)
    campsite = models.ForeignKey(Campsite, on_delete=models.CASCADE)

    def __str__(self):
        return f'Photo for campsite_id: {self.campsite_id} @{self.url}'