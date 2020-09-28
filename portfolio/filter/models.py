from django.db import models

class Artist(models.Model):
    artist = models.CharField(max_length=20)
class Gallery(models.Model):
    photo = models.ImageField(default="", upload_to="filter/")
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE, related_name="gallery_photo")
