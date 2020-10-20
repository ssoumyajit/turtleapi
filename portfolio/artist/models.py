from django.db import models
from django.conf import settings

class Artist(models.Model):
    artist_name = models.CharField(max_length=255)
    username = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

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