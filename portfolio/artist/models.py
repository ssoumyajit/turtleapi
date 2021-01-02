from django.db import models
from django.conf import settings
from user.models import User
from django_countries.fields import CountryField
import time
import datetime
import uuid

class Artist(models.Model):
    artist_name = models.CharField(max_length=255, default= "", blank = True)
    username = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="artist", blank = False ) #must
    artist_image = models.ImageField(default= "", upload_to = "covers/", blank = True)
    country = CountryField(default= "", blank = True)
    style = models.CharField(max_length = 15, default= "", blank = True)
    quote = models.CharField(max_length = 255, default= "", blank = True)
    introduction = models.TextField(default= "", blank = True)
    crew = models.CharField(max_length=255, default= "", blank = True)
    ig = models.URLField(max_length=200, default= "", blank = True)
    fb = models.URLField(max_length=200, default= "", blank = True)
    personal = models.URLField(max_length=200, default= "", blank = True)
    
    def __str__(self):
        return self.artist_name

class Gallery(models.Model):

    def scramble_uploaded_filename(self, file):

        now = str(int(time.time()))
        filepath = 'gallery/'
        extension = file.split(".")[-1]
        return "{}+{}.{}".format(filepath, uuid.uuid4(), extension)

    g_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # related_name="gallery") #manytoOne relationship
    g_upload_photo = models.ImageField(null =True,upload_to= scramble_uploaded_filename) 
    g_datetime = models.DateTimeField(auto_now = True)
    
    class Meta:
        ordering = ['-g_datetime']

class Highlights(models.Model):
    h_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #must
    h_context = models.CharField(max_length=255, default= "", blank = False) #must
    h_photo = models.ImageField(default= "", upload_to = "work/", blank = False) #must
    h_date = models.DateField(blank = True)
    h_content = models.TextField(default= "", blank = True)
    h_link = models.URLField(max_length=200, default= "",  blank = True)
    

    def __str__(self):
        return self.w_date

class JudgingWorkshop(models.Model):
    jw_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #must
    jw_event = models.CharField(max_length = 30,default= "", blank = False) #must
    jw_photo = models.ImageField(default= "", upload_to = "judgingworkshop/", blank = False) #must
    jw_date = models.DateField(blank = True)
    jw_content = models.TextField(default= "", blank = True)
    jw_link = models.URLField(max_length=200, default= "", blank = True)

    def __str__(self):
        return self.jw_date

class Events(models.Model):
    ev_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #must
    ev_event = models.CharField(max_length = 20, default= "", blank = False) #must
    ev_photo = models.ImageField(default= "", upload_to = "events_attended/", blank = False) #must
    ev_date = models.DateField(blank = True)
    ev_content = models.TextField(default= "", blank = True )
    ev_link = models.URLField(max_length=200, default= "", blank = True)

    def __str__(self):
        return self.ev_date


#null = True means, when u do not put anything in the field , it will be set NULL in the database
#blank = True/False   related only to the forms
#default = None, default=None does not allow or disallow a None value to be used. It simply tells #
#Django what should be the value of the field if it is not specified. null=True does allow None 
#to be used in the Python code. It is treated as NULL in the database. And you're right about blank being used for form validation. 

#gallery limit:
#https://stackoverflow.com/questions/31846152/limit-number-of-foreign-keys-based-on-how-many-foreign-keys-refer-to-that-model