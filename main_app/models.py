from django.db import models
from django.urls import reverse
from datetime import date


SOUNDS = (
    ('E', 'Epic'),
    ('C', 'Copacetic'),
    ('D', 'Defective')
)

class Concert(models.Model):
  venue = models.CharField(max_length=50)
  city = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('concerts_detail', kwargs={'pk': self.id})


class Vinyl(models.Model):
  name = models.CharField(max_length=100)
  artist = models.CharField(max_length=100)
  released = models.DateField()
  label = models.CharField(max_length=250)
  concerts = models.ManyToManyField(Concert)
  

  def __str__(self):
    return f'{self.name} ({self.id})'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'vinyl_id': self.id})

  def listen_for_today(self):
    return self.listening_set.filter(date=date.today()).count() >= len(SOUNDS)


class Listening(models.Model):
  date = models.DateField('Listening Date')
  sound = models.CharField(
    max_length=1,
    choices=SOUNDS,
    default=SOUNDS[0][0]
  )
  
  vinyl = models.ForeignKey(
    Vinyl,
    on_delete=models.CASCADE
  )

  def __str__(self):
    return f"{self.get_sound_display()} on {self.date}"

  class Meta:
    ordering = ['-date']


class Cover(models.Model):
  url = models.CharField(max_length=200)
  vinyl = models.ForeignKey(Vinyl, on_delete=models.CASCADE)

  def __str__(self):
    return f"Cover for vinyl_id: {self.vinyl_id} @{self.url}"

