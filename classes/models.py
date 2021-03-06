from django.db import models
from django.core.validators import FileExtensionValidator


class Level(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def get_friendly_name(self):
        return self.friendly_name


class Class(models.Model):

    class Meta:
        verbose_name_plural = 'Classes'

    level = models.ForeignKey('Level', null=True,
                              blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    duration = models.TimeField(null=True, blank=True)
    cover_image = models.ImageField(null=True, blank=True)
    cover_image_url = models.URLField(max_length=1024, null=True, blank=True)
    video = models.FileField(null=True, blank=True,
                             validators=[FileExtensionValidator(
                                 allowed_extensions=['MOV', 'avi', 'mp4',
                                                     'webm', 'mkv'])])
    video_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return str(self.name)
