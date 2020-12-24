from django.db import models
from django.conf import settings
from user.models import User
from django_countries.fields import CountryField
import time
import datetime
import uuid

class Sharing(models.Model):

    s_student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "student")
    s_teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "teacher", null=True)
    s_teacher_name = models.CharField(default="", max_length=255)
    s_teacher_country = CountryField()

    s_photo = models.ImageField(default="", upload_to = "sharing/")
    s_appreciation = models.CharField(max_length = 160, default = "") #1 line = 8 words, 20 lines to cover up the image
    s_video_talk = models.FileField(default="", upload_to = "talk/")
    s_video_dance = models.FileField(default="", upload_to = "dance/")

    s_date = models.DateField(auto_now = True)
    s_location = models.CharField(max_length = 30)
    
    voters_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = "votes")
        
    
    class Meta:
        ordering = ['s_date']


class Comments(models.Model):
    shareid = models.ForeignKey('Sharing', on_delete=models.CASCADE, related_name = "comment")
    commenter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = "commenter")
    comment = models.CharField(max_length = 255) #add a validation here.


