from django.db import models


class Movie(models.Model):

    title = models.CharField(max_length=250)
    released_year = models.PositiveSmallIntegerField()
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    genre = models.TextField()
    imdb_id = models.CharField(max_length=50, default="sa1")

    def __str__(self):
        return self.title
