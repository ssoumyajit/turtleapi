from django.db import models
from django.conf import settings
from user.models import User
from django_countries.fields import CountryField
import time
import datetime
import uuid

#for image manipulations
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
import os.path
from portfolio.settings import COVER_THUMBNAIL_SIZE

#trying with django_imagekit
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

class Artist(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="artist", blank = False)
    cover = models.ImageField(default= "", upload_to = "covers/", blank = True)
    thumb = models.ImageField(upload_to = "thumbnails/", blank = True, editable=False)
    country = CountryField(default= "", blank = True)
    artist_name =  models.CharField(max_length=255, default= "", blank = True)
    

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            raise Exception('could not create thumbnail, is the FileType valid ?')
        super(Artist, self).save(*args, **kwargs)

    def make_thumbnail(self):
            image = Image.open(self.cover)
            image.thumbnail(COVER_THUMBNAIL_SIZE, Image.ANTIALIAS)

            thumbnail_name, thumbnail_extension = os.path.splitext(self.cover.name)
            thumbnail_extension = thumbnail_extension.lower()
            thumbanil_filename = thumbnail_name + "_thumb" + thumbnail_extension

            if thumbnail_extension in ['.jpg', '.jpeg']:
                FTYPE = 'JPEG'
            elif thumbnail_extension == '.png':
                FTYPE = 'PNG'
            else:
                return False
            
            #save the thumbnail in memory file as StringIO
            temp_thumbnail = BytesIO()
            image.save(temp_thumbnail, FTYPE)
            temp_thumbnail.seek(0)
            
            # Load a ContetnFile into the thumbnail field so it gets saved.
            # set save=False, otherwise it will run in an infinite loop
            self.thumb.save(thumbanil_filename, ContentFile(temp_thumbnail.read()), save = False)
            temp_thumbnail.close()

            return True
            #https://stackoverflow.com/questions/23922289/django-pil-save-thumbnail-version-right-when-image-is-uploaded
    


class Bio(models.Model):
    b_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    b_style = models.CharField(max_length = 15, default= "", blank = True)
    b_quote = models.CharField(max_length = 255, default= "", blank = True)
    b_introduction = models.TextField(default= "", blank = True)
    b_crew = models.CharField(max_length=255, default= "", blank = True)
    b_ig = models.URLField(max_length=200, default= "", blank = True)
    b_fb = models.URLField(max_length=200, default= "", blank = True)
    b_personal = models.URLField(max_length=200, default= "", blank = True)

class Gallery(models.Model):

    def scramble_uploaded_filename(self, file):

        now = str(int(time.time()))
        filepath = 'gallery/'
        extension = file.split(".")[-1]
        return "{}+{}.{}".format(filepath, uuid.uuid4(), extension)

    g_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # related_name="gallery") #manytoOne relationship
    g_upload_photo = models.ImageField(null =True,upload_to= scramble_uploaded_filename) 
    g_datetime = models.DateTimeField(auto_now = True)

    def save(self, *args, **kwargs):
        super(Gallery, self).save(*args, **kwargs)
        photo = Image.open(self.g_upload_photo.path) 
        photo.thumbnail((240,240), Image.ANTIALIAS)
        photo.save(self.g_upload_photo.path, optimize = True, quality = 90)
    
    class Meta:
        ordering = ['-g_datetime']

class Highlights(models.Model):
    h_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #must
    h_context = models.CharField(max_length=255, default= "", blank = False) #must
    h_photo = models.ImageField(default= "", upload_to = "work/", blank = False) #must
    h_date = models.DateField(null=True, blank = True)  #blank is for admin, null is for db.
    h_content = models.TextField(default= "", blank = True)
    h_link = models.URLField(max_length=200, default= "",  blank = True)

    def save(self, *args, **kwargs):
        super(Highlights, self).save(*args, **kwargs)
        photo = Image.open(self.h_photo.path) 
        photo.thumbnail((240,180), Image.ANTIALIAS)
        photo.save(self.h_photo.path, optimize = True, quality = 90)

        #photo.save(self.h_photo.path,format="PNG", optimize=True, quality=10)
        #if photo.mode != "RGB":
                #photo.convert('RGB')
    

    def __str__(self):
        return self.h_date

class JudgingWorkshop(models.Model):
    jw_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #must
    jw_event = models.CharField(max_length = 30,default= "", blank = False) #must
    jw_photo = models.ImageField(default= "", upload_to = "judgingworkshop/", blank = False) #must
    jw_date = models.DateField(null =True, blank = True)
    jw_content = models.TextField(default= "", blank = True)
    jw_link = models.URLField(max_length=200, default= "", blank = True)

    def save(self, *args, **kwargs):
        super(Highlights, self).save(*args, **kwargs)
        photo = Image.open(self.jw_photo.path) 
        photo.thumbnail((240,180), Image.ANTIALIAS)
        photo.save(self.jw_photo.path, optimize = True, quality = 90)

    def __str__(self):
        return self.jw_date

class Events(models.Model):
    ev_artist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #must
    ev_event = models.CharField(max_length = 20, default= "", blank = False) #must
    ev_photo = models.ImageField(default= "", upload_to = "events_attended/", blank = False) #must
    ev_date = models.DateField(null = True,blank = True)
    ev_content = models.TextField(default= "", blank = True )
    ev_link = models.URLField(max_length=200, default= "", blank = True)

    def save(self, *args, **kwargs):
        super(Highlights, self).save(*args, **kwargs)
        photo = Image.open(self.ev_photo.path) 
        photo.thumbnail((240,180), Image.ANTIALIAS)
        photo.save(self.ev_photo.path, optimize = True, quality = 90)

    def __str__(self):
        return self.ev_date


#null = True means, when u do not put anything in the field , it will be set NULL in the database
#blank = True/False   related only to the forms
#default = None, default=None does not allow or disallow a None value to be used. It simply tells #
#Django what should be the value of the field if it is not specified. null=True does allow None 
#to be used in the Python code. It is treated as NULL in the database. And you're right about blank being used for form validation. 

#gallery limit:
#https://stackoverflow.com/questions/31846152/limit-number-of-foreign-keys-based-on-how-many-foreign-keys-refer-to-that-model

