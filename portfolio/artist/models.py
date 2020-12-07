from django.db import models
from django.conf import settings
from user.models import User
from django_countries.fields import CountryField
import time
import datetime
import uuid

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    username = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="artist" )
    artist_image = models.ImageField(default="", upload_to = "covers/")
    country = CountryField()
    style = models.CharField(max_length = 15, default = "")
    quote = models.CharField(max_length = 255, default="")
    introduction = models.TextField(default= "")
    
    def __str__(self):
        return self.artist_name

class Gallery(models.Model):

    def scramble_uploaded_filename(self, file):

        now = str(int(time.time()))
        filepath = 'gallery/'
        extension = file.split(".")[-1]
        return "{}+{}.{}".format(filepath, uuid.uuid4(), extension)

    g_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # related_name="gallery") #manytoOne relationship
    g_upload_photo = models.ImageField(default="",upload_to= scramble_uploaded_filename )
    g_datetime = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-g_datetime']

class Work(models.Model):
    w_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    w_context = models.CharField(max_length=255)
    w_photo = models.ImageField(default="", upload_to = "work/")
    w_datetime = models.DateTimeField(auto_now = True)
    w_content = models.TextField()


    def __str__(self):
        return self.wcontext