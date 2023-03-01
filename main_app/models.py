from django.db import models
from django.urls import reverse


class Vinyl(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    released = models.DateField()
    label = models.CharField(max_length=100)


def __str__(self):
    return f'{self.name} ({self.id})'

def get_absolute_url(self):
    return reverse('detail', kwargs={'vinyl_id': self.id})
