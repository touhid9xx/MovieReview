from django.db import models

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/')
    director = models.CharField(max_length=300)
    cast = models.CharField(max_length=500)
    description = models.TextField(max_length=5000)
    release_date = models.DateField()
    averageRating = models.FloatField(default=0)

    def __str__(self):
        return self.name
    
    def __unicode__(self):
        return self.name

   