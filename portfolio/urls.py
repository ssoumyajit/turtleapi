"""portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import serializers, viewsets, routers
from django.db import models
from django_countries.fields import CountryField
import datetime

from django.conf import settings
from django.conf.urls.static import static

import uuid  #hashing the imagefilenames


#-----------Utility Functions----------------#
#write a function which will hash (not exactly hashing but kind of generate a random string) the file names of the images instead of showing the actual names...security 
#you need to make migrations after this... django thing.
#u can change the name of the new migration and run migrate after that...done
def scramble_uploaded_filename(instance, filename):
    extension = filename.split(".")[-1]
    #return "{},{}".format(stringified_file_name, extension)
    return "{}.{}".format(uuid.uuid4(), extension)
#-----------Utility Functions----------------#

w_dancestyles = (
    ("",""),
    ("HipHop","HipHop"),
    ("HipHop Freestyle","HipHop Freestyle"),
    ("Breaking","Breaking"),
    ("House","House"),  
    ("Locking","Locking"),
    ("Popping","Popping"),
    ("Waacking","Waacking"),
    ("Krump","Krump"),
    ("Vouge","Vouge"),
    ("Litefeet","Litefeet"),
    ("Tutting","Tutting"),
    ("Flexing","Flexing"),
    ("Footwork","Footwork"),
    ("Handstyle","Handstyle"),
    ("Waving","Waving"),
    ("Animation","Animation"),
    ("Urban","Urban"),
    ("Choreography","Choreography"),
    ("Freestyle","Freestyle"),
    ("Afro","Afro"),
    ("Jazz","Jazz"),
    ("Salsa","Salsa"),
    ("Contemporary","Contemporary"),
    ("Experimental","Experimental"),  
)


#cretae a simple model
class Portfolio(models.Model):
    artist_name = models.CharField(max_length = 20)
    #country = models.CharField(max_length = 20)
    country = CountryField()
    style = models.CharField(max_length = 15, default = "")
    artist_image = models.FileField(default="", upload_to='portfolio/images/scramble_uploaded_filename')
    bio = models.CharField(max_length = 100, default="")
    #seems like  required=True by default


class Workshop(models.Model):
    w_name = models.CharField(max_length = 50)
    w_dancestyle = models.CharField(max_length = 50, 
        choices = w_dancestyles, 
        default = "")
    w_content = models.CharField(max_length = 50)
    w_teacher = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name= "workshop")
    w_country = CountryField()
    w_location = models.CharField(max_length = 20)
    w_date = models.DateTimeField()
    w_photo = models.ImageField(default="",upload_to='workshop/images/scramble_uploaded_filename')
    ##,width_field= 50, height_field = 50  : does not work when I try to upload via API 


#all the events where this artist was/is/will be a judge.
class Judging(models.Model):
    j_judge = models.ForeignKey(Portfolio, on_delete= models.CASCADE, related_name = "judge" )
    j_event_name = models.CharField(max_length = 50)
    j_dancestyle = models.CharField(max_length = 50, 
        choices = w_dancestyles, 
        default = "")
    j_country = CountryField()
    j_location = models.CharField(max_length = 20)
    j_date = models.DateField()
    j_event_photo =  models.ImageField(default="",upload_to='judging/images/scramble_uploaded_filename')
    #other judges , future feature


class Gallery(models.Model):
    g_artist = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="gallery") #manytoOne relationship
    g_upload_photo = models.ImageField(default="",upload_to='gallery/images/scramble_uploaded_filename')
    g_datetime = models.DateTimeField(auto_now = True) #last modified timestamp

class Milestone(models.Model):
    m_artist = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="milestone")
    m_what_happend = models.CharField(max_Length = 100)
    m_context = models.CharField(default = "", max_length = 500)
    m_date = models.DateField(default = "")
    m_photo = models.ImageField(default= "", upload_to = 'milestone/scramble_uploaded_filename')

class ThoughtSnippet():
    t_artist = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name="thoughtsnippets")
    t_title = models.CharField(max_length = 100)
    t_content = models.CharField(max_length = 50000)
    t_photo = models.ImageField(default = "", upload_to = 'thoughtsnippet/scramble_uploaded_filename')
    t_date = models.DateField()
#------------------------------------------------------------------------------------


class WorkshopSerializers(serializers.ModelSerializer):
    class Meta:
        model = Workshop
        fields = "__all__"
        #depth = 1

class JudgingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Judging
        fields = "__all__"
        #depth = 1

class GallerySerializers(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = "__all__"
        #depth = 1


class MilestoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = "__all__"


class ThoughtSnippetSerializers(serializers.ModelSerializer):
    class Meta:
        model = ThoughtSnippet
        fields = "__all__"

class PortfolioSerializers(serializers.HyperlinkedModelSerializer):
    workshop = WorkshopSerializers(many = True, read_only = True)
    judge = JudgingSerializers(many = True, read_only = True)
    gallery = GallerySerializers(many = True, read_only = True)

    class Meta:
        model = Portfolio
        fields = ("id", "artist_name","country", "style" ,"artist_image", "bio", \
            "gallery","workshop", "judge")
    

#------------------------------------------------------------------------------


class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializers

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset =  Workshop.objects.all()
    serializer_class = WorkshopSerializers

class JudgingViewSet(viewsets.ModelViewSet):
    serializer_class = JudgingSerializers
    queryset = Judging.objects.all()

class GalleryViewSet(viewsets.ModelViewSet):
    serializer_class = GallerySerializers
    queryset = Gallery.objects.all()

class MilestoneViewSet(viewsets.ModelViewSet):
    serializer_class = MilestoneSerializers
    query_set = Milestone.objects.all()

class ThoughtSnippetViewset(viewsets.ModelViewSet):
    serializer_class = ThoughtSnippetSerializers
    query_set = ThoughtSnippet.objects.all()

#------------------------------------------------------------------------------

router = routers.DefaultRouter()
router.register(r'portfolio', PortfolioViewSet)
router.register(r'workshop', WorkshopViewSet)
router.register(r'judging', JudgingViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'milestone', MilestoneViewSet)
router.register(r'thoughts', ThoughtSnippetViewset)
#router.register(r'gallery/images', GalleryViewSet)

#wire up the API using automatic URL routing
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]

#configure before production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)