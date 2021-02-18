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
from rest_framework import generics  #for gallery filtering.
from django_countries.fields import CountryField
#from django_countries.serializer_fields import CountryField #don't keep both CountryField
#from django_countries.serializers import CountryFieldMixin
import datetime

from django.conf import settings
from django.conf.urls.static import static

import uuid  #hashing the imagefilenames

from io import BytesIO
from PIL import Image
from django.core.files import File

import sys
import time
import os  #during PIL operations

from rest_framework.parsers import JSONParser, MultiPartParser, FormParser
from django.db.models import TextField
from rest_framework import filters

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

#global variables----------------------------
photo='portfolio/photo_comment.png'


#-----------Utility Functions----------------#
#write a function which will hash (not exactly hashing but kind of generate a random string) the file names of the images instead of showing the actual names...security 
#you need to make migrations after this... django thing.
#u can change the name of the new migration and run migrate after that...done


#utility function for image resizing and compression

def resize_compress(image):
    img = Image.open(image)
    img_io = BytesIO()  #one instance of BytesIO class
    img.save(img_io, "JPEG", quality = 60)
    new_img = File(img_io, name = image.name)
    return new_img

class NonStrippingTextField(TextField):
    """A TextField that does not strip whitespace at the beginning/end of
    it's value.  Might be important for markup/code."""

    def formfield(self, **kwargs):
        kwargs['strip'] = False
        return super(NonStrippingTextField, self).formfield(**kwargs)

#-----------Utility Functions----------------#


w_dancestyles = (
    ("", ""),
    ("HipHop", "HipHop"),
    ("HipHop Freestyle", "HipHop Freestyle"),
    ("Breaking", "Breaking"),
    ("House", "House"),
    ("Locking", "Locking"),
    ("Popping", "Popping"),
    ("Waacking", "Waacking"),
    ("Krump", "Krump"),
    ("Vouge", "Vouge"),
    ("Litefeet", "Litefeet"),
    ("Tutting", "Tutting"),
    ("Flexing", "Flexing"),
    ("Footwork", "Footwork"),
    ("Handstyle", "Handstyle"),
    ("Waving", "Waving"),
    ("Animation", "Animation"),
    ("Urban", "Urban"),
    ("Choreography", "Choreography"),
    ("Freestyle", "Freestyle"),
    ("Afro", "Afro"),
    ("Jazz", "Jazz"),
    ("Salsa", "Salsa"),
    ("Contemporary", "Contemporary"),
    ("Experimental", "Experimental"),
)

#cretae a simple model
class Portfolio(models.Model):
    
    #take this function outside the class and implement DRY
    def scramble_uploaded_filename(self, filename):
        folder = "portfolio/"
        extension = filename.split(".")[-1]
        #return "{},{}".format(stringified_file_name, extension)
        return "{}+{}.{}".format(folder, uuid.uuid4(), extension)

    artist_name = models.CharField(max_length = 20)
    #country = CountryField(blank_label='(select country)')
    #country = CountryField(country_dict=True)
    username = models.CharField(max_length = 20, unique=True)
    country = CountryField()
    style = models.CharField(max_length = 15, default = "")
    artist_image = models.FileField(default="", upload_to = scramble_uploaded_filename) 
                                       #we don't want to call the scramle__ function {no bracket()}, we just need to reference it
                                       #so that every time an image is uploaded, django image field will itself call it.
    bio = models.CharField(max_length = 100, default="")
    introduction = models.TextField(default= "")
    
    #seems like  required=True by default
    #https://pydigger.com/pypi/django-countries
    #https://stackoverflow.com/questions/36080198/django-countries-and-tastypie-get-country-name
    #https://stackoverflow.com/questions/33563876/how-to-dehydrate-a-django-model-fieldname
    #https://groups.google.com/g/django-rest-framework/c/3hrS2xr6BS0
    #https://github.com/SmileyChris/django-countries/issues/106
    #https://pynative.com/make-python-class-json-serializable/

    def __str__(self):
        return self.artist_name

class Workshop(models.Model):

    def scramble_uploaded_filename(self, filename):
        folder = "workshop/"
        extension = filename.split(".")[-1]
        #return "{},{}".format(stringified_file_name, extension)
        return "{}+{}.{}".format(folder, uuid.uuid4(), extension)

    w_name = models.CharField(max_length = 50)
    w_dancestyle = models.CharField(max_length = 50, 
        choices = w_dancestyles, 
        default = "")
    w_content = models.CharField(max_length = 50)
    w_teacher = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name= "workshop")
    w_country = CountryField()
    w_location = models.CharField(max_length = 20)
    w_date = models.DateTimeField()
    w_photo = models.ImageField(default="",upload_to=scramble_uploaded_filename)
    ##,width_field= 50, height_field = 50  : does not work when I try to upload via API 
    
    def __str__(self):
        return self.w_name

    def save(self, *args, **kwargs):
        w_photo = resize_compress(self.w_photo)
        self.w_photo = w_photo
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-w_date']


#all the events where this artist was/is/will be a judge.
class Judging(models.Model):

    def scramble_uploaded_filename(self, filename):
        folder = "judging/"
        extension = filename.split(".")[-1]
        #return "{},{}".format(stringified_file_name, extension)
        return "{}+{}.{}".format(folder, uuid.uuid4(), extension)

    j_judge = models.ForeignKey('Portfolio', on_delete= models.CASCADE, related_name = "judge" )
    j_event_name = models.CharField(max_length = 50)
    j_dancestyle = models.CharField(max_length = 50, 
        choices = w_dancestyles, 
        default = "")
    j_country = CountryField()
    j_location = models.CharField(max_length = 20)
    j_date = models.DateField()
    j_event_photo =  models.ImageField(default="",upload_to=scramble_uploaded_filename)
    #other judges , future feature
    def __str__(self):
        return self.j_event_name

    def save(self, *args, **kwargs):
        j_event_photo = resize_compress(self.j_event_photo)
        self.j_event_photo = j_event_photo
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-j_date']


class Gallery(models.Model):
    
    #resizedphoto = 'gallery/resized/'  #resized photo path

    def scramble_uploaded_filename(self, file):

        now = str(int(time.time()))
        #filepath = 'gallery/'+ now +'/'
        filepath = 'gallery/'
        extension = file.split(".")[-1]
        #return "{},{}".format(stringified_file_name, extension)
        return "{}+{}.{}".format(filepath, uuid.uuid4(), extension)
    

    g_artist = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name="gallery") #manytoOne relationship
    g_upload_photo = models.ImageField(default="",upload_to= scramble_uploaded_filename )
    g_datetime = models.DateTimeField(auto_now = True) #last modified timestamp


    '''
    def save(self, *args, **kwargs):
        super(Gallery, self).save(*args, **kwargs)
        photo = Image.open(self.g_upload_photo.path)
        photo.thumbnail((480,360), Image.ANTIALIAS)
        photo.save(self.g_upload_photo.path)
    '''
    class Meta:
        ordering = ['-g_datetime']
    
    #http://www.mechanicalgirl.com/post/image-resizing-file-uploads-doing-it-easy-way/


class Milestone(models.Model):

    def scramble_uploaded_filename(self, filename):
        folder = "milestone/"
        extension = filename.split(".")[-1]
        #return "{},{}".format(stringified_file_name, extension)
        return "{}+{}.{}".format(folder, uuid.uuid4(), extension)
    
    m_artist = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name="milestone")
    m_what_happend = models.CharField(max_length = 100)
    m_context = models.CharField(default = "", max_length = 255)
    m_date = models.DateField(default = "")
    m_photo = models.ImageField(default= "", upload_to = scramble_uploaded_filename)
    

    class Meta:
        ordering = ['-m_date']

class Thought(models.Model):

    def scramble_uploaded_filename(self, filename):
        folder = "thought/"
        extension = filename.split(".")[-1]
        #return "{},{}".format(stringified_file_name, extension)
        return "{}+{}.{}".format(folder, uuid.uuid4(), extension)

    t_artist = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name="thought")
    t_title = models.CharField(max_length = 100)
    t_content = models.CharField(max_length = 50000)
    t_photo = models.ImageField(default = "", upload_to = scramble_uploaded_filename)
    t_date = models.DateField()

    def __str__(self):
        return self.t_title

    def save(self, *args, **kwargs):
        t_photo = resize_compress(self.t_photo)
        self.t_photo = t_photo
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-t_date']


#------------------------------------ today's project --------------------------------#


#class share_is_care
class Sharing(models.Model):
    
    #This one is not being used here, coz It is NOT being called at upload_to parameter
    def scramble_uploaded_filename(self, filename):
        folder = "thought/"
        extension = filename.split(".")[-1]
        #return "{},{}".format(stringified_file_name, extension)
        return "{}+{}.{}".format(folder, uuid.uuid4(), extension)

    s_photo = models.ImageField(default="", upload_to = "sharing/")
    s_student = models.ManyToManyField('Portfolio', related_name = "mystudent")
    s_teacher = models.ManyToManyField('Portfolio', related_name= "myteacher")
    s_appreciation = models.CharField(max_length = 160, default = "") #1 line = 8 words, 20 lines to cover up the image
    s_where_u_met = models.CharField(max_length = 100, default = "") #in future when event product is created, may be make it dynamic
    s_date = models.DateField()
    s_country = CountryField()
    s_location = models.CharField(max_length = 30)
    s_photo_comment = models.ImageField(default = "", upload_to = "sharing/")

        
    
    class Meta:
        ordering = ['s_date']
    
    '''
    def save(self, *args, **kwargs):
        #super(Sharing, self).save(*args, **kwargs)        
        size = (50,50)
        #file, ext = os.path.splitext(photo)
        k = Image.open(photo) #returns an image object.
        k.resize(size)   #do some operations on image object.
        img_io = BytesIO()
        new_img = File(img_io, name = photo.name)
        self.s_photo_comment = new_img
        #self.s_photo_comment = k.save(img_io + '.resized', "PNG")  #(file, "PNG")here file is a/b/c/name
        super().save(*args, **kwargs)



        img = Image.open(image)
        img_io = BytesIO()  #one instance of BytesIO class
        img.save(img_io, "JPEG", quality = 60)
        new_img = File(img_io, name = image.name)
        return new_img
'''
    

class Blog(models.Model):
    b_user = models.ForeignKey('Portfolio', on_delete=models.CASCADE, related_name="blog")
    b_title = models.CharField(max_length = 255, default = "" )
    b_date = models.DateField()
    b_content = models.TextField(default = "")
    b_photo = models.ImageField(default = "", upload_to = "blog/")

    class Meta:
        ordering = ['b_date']

class Biography(models.Model):
    bi_user = models.OneToOneField('Portfolio', on_delete = models.CASCADE, primary_key = True)
    bi_content = NonStrippingTextField()
    bi_photo1 = models.ImageField(default = "", upload_to = 'biography/')
    #eventually will put more photos, videos, links etc.

class Fileupload(models.Model):
    file = models.ImageField(default = "", upload_to = "uploads/")
    text = models.CharField(default = "", max_length = 255)
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
        #depth = 1 #when you keep this depth option, it implies read only..so u won't be able
        #to get all the fields while upaloding via browsabel api.

        #fields = ['pk','g_artist', 'g_upload_photo', 'g_resized_photo_path']
        #read_only= ['g_resized_photo_path']
        # extra_kwargs = {
            #'g_resized_photo_path': {'write_only': True}
        #}
        depth = 1


class MilestoneSerializers(serializers.ModelSerializer):
    class Meta:
        model = Milestone
        fields = "__all__"


class ThoughtSerializers(serializers.ModelSerializer):
    class Meta:
        model = Thought
        fields = "__all__"

class SharingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sharing
        #exclude = ['s_photo_comment']
        fields = "__all__"
        depth=1

class FileuploadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fileupload
        fields = "__all__"

class BlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class BiographySerializers(serializers.ModelSerializer):
    #bi_content = serializers.TextField(trim_whitespace=False)
    class Meta:
        model = Biography
        fields = "__all__"
        #extra_kwargs = {"bi_content": {"trim_whitespace": False}}

#class PortfolioSerializers(serializers.HyperlinkedModelSerializer):
class PortfolioSerializers(serializers.ModelSerializer):
    '''
    workshop = WorkshopSerializers(many = True, read_only = True)
    judge = JudgingSerializers(many = True, read_only = True)
    gallery = GallerySerializers(many = True, read_only = True)
    milestone = MilestoneSerializers(many = True, read_only = True)
    biography = BiographySerializers(read_only = True)
    #thought = ThoughtSerializers(many = True, read_only = True)
    myteacher = SharingSerializers(many = True, read_only = True) #source = "portfolio_set"
    mystudent = SharingSerializers(many = True, read_only = True) #source = "portfolio_set"
    #read_only : it is for get and retrieve actions, only reading, no writing.
    '''
    class Meta:
        model = Portfolio
        fields = "__all__"
        #fields = ("id", "artist_name", "username" ,"country", "style" ,"artist_image", "bio","introduction","biography", \
        #    "gallery","workshop", "judge", "milestone", "myteacher", "mystudent", )
        #depth = 2


#------------------------------------------------------------------------------
class PortfolioViewSet(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)   
    serializer_class = PortfolioSerializers
    lookup_field = "username"
    queryset = Portfolio.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class WorkshopViewSet(viewsets.ModelViewSet):
    queryset =  Workshop.objects.all()
    serializer_class = WorkshopSerializers

class JudgingViewSet(viewsets.ModelViewSet):
    queryset = Judging.objects.all()
    serializer_class = JudgingSerializers
         
class GalleryViewSet(viewsets.ModelViewSet):
    #lookup_field = "g_artist"
    #def get_queryset(self):
        #return Gallery.objects.filter()
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['g_artist__username']

'''
#filtering against query_set
# http://example.com/api/purchases?username=denvercoder9
class GalleryListView(generics.ListAPIView):
    serializer_class = GallerySerializers

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Gallery.objects.all()
        username = self.request_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(g_artist__username=username)
        return queryset
'''


#filtering against url...looks clean
#https://docs.djangoproject.com/en/2.2/topics/db/queries/#lookups-that-span-relationships

'''
class GalleryListView(generics.ListAPIView):
    serializer_class = GallerySerializers
    #filter_fields = ('username',)  #the string that u r using to search in url.
    filter_fields = ('g_artist',)

    def get_queryset(self):
        """
        This view should return a list of all gallery photos,
        for the artist as determined by the artist name.
        """
        username = self.kwargs['username']
        return Gallery.objects.filter(portfolio__username = username)
'''



class MilestoneViewSet(viewsets.ModelViewSet):
    queryset = Milestone.objects.all()
    serializer_class = MilestoneSerializers
    
class ThoughtViewset(viewsets.ModelViewSet):
    queryset = Thought.objects.all()
    serializer_class = ThoughtSerializers

class SharingViewSet(viewsets.ModelViewSet):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['s_teacher__username', 's_student__username']

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializers

class BiographyViewSet(viewsets.ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographySerializers

class FileuploadViewSet(viewsets.ModelViewSet):
    #parser_classes = (MultiPartParser, FormParser)
    queryset = Fileupload.objects.all()
    serializer_class = FileuploadSerializers
#------------------------------------------------------------------------------

router = routers.DefaultRouter()

"""
router.register(r'portfolio', PortfolioViewSet)
router.register(r'workshop', WorkshopViewSet)
router.register(r'judging', JudgingViewSet)
router.register(r'gallery', GalleryViewSet)
router.register(r'milestone', MilestoneViewSet)
#router.register(r'thought', ThoughtViewset)
router.register(r'sharing', SharingViewSet)
router.register(r'blog', BlogViewSet)
router.register(r'biography', BiographyViewSet)


router.register(r'fileupload', FileuploadViewSet)
#router.register(r'portfoliomini', PortfolioMiniViewSet)
"""

# wire up the API using automatic URL routing
urlpatterns = [
    # path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api/v1/user/', include('user.urls')),
    path('api/v1/artist/', include('artist.urls')),
    path('api/v1/e1t1/', include('sharing.urls')),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]

# configure before production
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    # this line helps to avail media url in our development server and we dont need a separate
    # webserver just to serve image files


'''
        
    def save(self, *args, **kwargs):
        super(Sharing, self).save(*args, **kwargs)
        photo = Image.open(self.s_photo.path)
        photo.thumbnail((128,128), Image.ANTIALIAS)
        photo.save(self.s_photo.path)

        #photo_comment = Image.open(self.s_photo_comment.path)
        photo_comment = "photo_comment.png"
        fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
        d = ImageDraw.Draw(photo_comment)
        d.multiline_text((10,10), "self.s_appreciation", font=fnt, fill=(0, 0, 0), spacing=4, align='left')
        d.save(self.s_photo_comment.path)
        #Thumbnail() takes a sizes tuple (w, h) and an optional filter as arguments. 
        #When thumbnail() resizes, it produces an image no larger than the given 
        #dimensions, and maintains the original aspect. Problem solved!
'''
'''
    #import os
    #from io import BytesIO
    #from PIL import Image, ExifTags
    
    EXIF_ORIENTATION = 274  # Magic numbers from http://www.exiv2.org/tags.html
    
    def random_hex_bytes(n_bytes):
        """Create a hex encoded string of random bytes"""
        return os.urandom(n_bytes).hex()
    
    def resize_image(file_p, size):
        """Resize an image to fit within the size, and save to the path directory"""
        dest_ratio = size[0] / float(size[1])
        try:
            image = Image.open(file_p)
        except IOError:
            print("Error: Unable to open image")
            return None
    
        try:
            exif = dict(image._getexif().items())
            if exif[EXIF_ORIENTATION] == 3:
                image = image.rotate(180, expand=True)
            elif exif[EXIF_ORIENTATION] == 6:
                image = image.rotate(270, expand=True)
            elif exif[EXIF_ORIENTATION] == 8:
                image = image.rotate(90, expand=True)
        except:
            print("No exif data")
    
        source_ratio = image.size[0] / float(image.size[1])
    
        # the image is smaller than the destination on both axis
        # don't scale it
        if image.size < size:
            new_width, new_height = image.size
        elif dest_ratio > source_ratio:
            new_width = int(image.size[0] * size[1]/float(image.size[1]))
            new_height = size[1]
        else:
            new_width = size[0]
            new_height = int(image.size[1] * size[0]/float(image.size[0]))
        image = image.resize((new_width, new_height), resample=Image.LANCZOS)
    
        final_image = Image.new("RGBA", size)
        topleft = (int((size[0]-new_width) / float(2)),
                   int((size[1]-new_height) / float(2)))
        final_image.paste(image, topleft)
        bytes_stream = BytesIO()
        final_image.save(bytes_stream, 'PNG')
        return bytes_stream.getvalue()
'''      
