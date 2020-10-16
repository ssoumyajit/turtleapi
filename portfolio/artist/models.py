from django.db import models
from django.conf import settings

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    name = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    def __str__(self):
        return self.artist_name

