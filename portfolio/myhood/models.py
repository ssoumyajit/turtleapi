from django.db import models
from django.conf import settings
from user.models import User

class MyHood(models.Model):
    teacher = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="myhood" )
    myhood =  models.CharField(max_length=255)
    def __str__(self):
        return self.myhood

class Students(models.Model):
    belongs_to = models.ForeignKey(MyHood, on_delete=models.CASCADE)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.student

class Post(Students):
    #poster = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="post")
    content = models.TextField()

