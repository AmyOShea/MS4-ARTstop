from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=254)
    artist_statement = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField()
    instagram_url = models.URLField(max_length=1024, null=True, blank=True)
    facebook_url = models.URLField(max_length=1024, null=True, blank=True)
    youtube_url = models.URLField(max_length=1024, null=True, blank=True)
    twitter_url = models.URLField(max_length=1024, null=True, blank=True)
    linkedin_url = models.URLField(max_length=1024, null=True, blank=True)
    website_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
