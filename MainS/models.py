from pyexpat import model
from django.db import models

class Songs(models.Model):
    Track_Name = models.CharField(max_length=100)
    Artist_Name = models.CharField(max_length=50)
    Genre = models.CharField(max_length=50)
    Beats_Per_Minute = models.IntegerField()
    Energy = models.IntegerField()
    Danceability = models.IntegerField()
    Loudness = models.IntegerField()
    Liveness = models.IntegerField()
    Valence = models.IntegerField()
    Length = models.IntegerField()
    Acousticness = models.IntegerField()
    Speechiness = models.IntegerField()
    Popularity = models.IntegerField()