from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=254)
    artist_statement = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()

    def __str__(self):
        return self.name
