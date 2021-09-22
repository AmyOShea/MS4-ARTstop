from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=254)
    artist_statement = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
