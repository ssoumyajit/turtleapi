from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
import time
import uuid

# for image manipulations
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO
import os.path
from portfolio.settings import COVER_THUMBNAIL_SIZE


def scramble_uploaded_filename(file):

    now = str(int(time.time()))
    filepath = 'gallery/'
    extension = file.split(".")[-1]
    return "{}+{}.{}".format(filepath, uuid.uuid4(), extension)


class Artist(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="artist", blank=False)
    cover = models.ImageField(default="", upload_to="covers/", blank=True)
    thumb = models.ImageField(upload_to="thumbnails/", blank=True, editable=False)
    country = CountryField(default="", blank=True)
    artist_name = models.CharField(max_length=255, default="", blank=True)

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            raise Exception('could not create thumbnail, is the FileType valid ?')
        super(Artist, self).save(*args, **kwargs)

    def make_thumbnail(self):
        image = Image.open(self.cover)
        image.thumbnail(COVER_THUMBNAIL_SIZE, Image.ANTIALIAS)
        thumbnail_name, thumbnail_extension = os.path.splitext(self.cover.name)
        thumbnail_extension = thumbnail_extension.lower()
        thumbnail_filename = thumbnail_name + "_thumb" + thumbnail_extension

        if thumbnail_extension in ['.jpg', '.jpeg']:
            filetype = 'JPEG'
        elif thumbnail_extension == '.png':
            filetype = 'PNG'
        else:
            return False

        # save the thumbnail in memory file as StringIO
        temp_thumbnail = BytesIO()
        image.save(temp_thumbnail, filetype)
        temp_thumbnail.seek(0)

        # Load a ContentFile into the thumbnail field so it gets saved.
        # set save=False, otherwise it will run in an infinite loop
        self.thumb.save(thumbnail_filename, ContentFile(temp_thumbnail.read()), save=False)
        temp_thumbnail.close()
        return True
        # https://stackoverflow.com/questions/23922289/django-pil-save-thumbnail-version-right-when-image-is-uploaded


class ArtistData(models.Model):
    username = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="artistdata")
    style = models.CharField(max_length=15, default="", blank=True)
    quote = models.CharField(max_length=255, default="", blank=True)
    introduction = models.TextField(default="", blank=True)
    crew = models.CharField(max_length=255, default="", blank=True)
    ig = models.URLField(max_length=200, default="", blank=True)
    fb = models.URLField(max_length=200, default="", blank=True)
    site = models.URLField(max_length=200, default="", blank=True)
    gallery1 = models.ImageField(null=True, blank=True, upload_to='gallery/')
    gallery2 = models.ImageField(null=True, blank=True, upload_to='gallery/')
    gallery3 = models.ImageField(null=True, blank=True, upload_to='gallery/')
    gallery4 = models.ImageField(null=True, blank=True, upload_to='gallery/')

    """
        def save(self, *args, **kwargs):
        super(ArtistData, self).save(*args, **kwargs)
        gallery1 = Image.open(self.gallery1.path)
        gallery1.thumbnail((240, 240), Image.ANTIALIAS)
        gallery1.save(self.gallery1.path, optimize=True, quality=90)
    """


class Highlights(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # must
    hicontext = models.CharField(max_length=255, default="", blank=False)  # must
    hiphoto = models.ImageField(default="", upload_to="work/", blank=False)  # must
    hidate = models.DateField(null=True, blank=True)  # blank is for admin, null is for db.
    hicontent = models.TextField(default="", blank=True)
    hilink = models.URLField(max_length=200, default="",  blank=True)
    # add 5 photos to really talk about this highlight of yours.
    # make 2 different serializers where the 2nd one will be used to
    # fetch these extra photos only when retrieved... that means when the user clicks on this card.

    def save(self, *args, **kwargs):
        super(Highlights, self).save(*args, **kwargs)
        photo = Image.open(self.h_photo.path) 
        photo.thumbnail((240, 180), Image.ANTIALIAS)
        photo.save(self.h_photo.path, optimize=True, quality=90)

    def __str__(self):
        return self.h_date


class Journey(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)  # must
    joevent = models.CharField(max_length=255, default="", blank=False)  # must
    jophoto = models.ImageField(default="", upload_to="events_attended/", blank=False)  # must
    jodate = models.DateField(null=True, blank=True)
    jocontent = models.TextField(default="", blank=True)
    jolink = models.URLField(max_length=255, default="", blank=True)

    def save(self, *args, ** kwargs):
        super(Journey, self).save(*args, **kwargs)
        photo = Image.open(self.jophoto.path)
        photo.thumbnail((240, 180), Image.ANTIALIAS)
        photo.save(self.jophoto.path, optimize=True, quality=90)

    def __str__(self):
        return self.jodate


# null = True means, when u do not put anything in the field , it will be set NULL in the database
# blank = True/False   related only to the forms
# default = None, default=None does not allow or disallow a None value to be used. It simply tells #
# Django what should be the value of the field if it is not specified. null=True does allow None
# to be used in the Python code. It is treated as NULL in the database. And you're right about blank being used for form validation.

# gallery limit:
# https://stackoverflow.com/questions/31846152/limit-number-of-foreign-keys-based-on-how-many-foreign-keys-refer-to-that-model

