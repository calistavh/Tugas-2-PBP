from django.db import models

class WatchlistMovie(models.Model):
    watched = models.CharField(max_length=3)
    title = models.CharField(max_length=50)
    rating = models.CharField(max_length=1)
    release_date = models.CharField(max_length=20)
    review = models.TextField()