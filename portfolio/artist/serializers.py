from rest_framework import serializers
from artist.models import Artist, Gallery, Work
from user.serializers import UserSerializer

class ArtistSerializers(serializers.ModelSerializer):
    '''
    dedicated artist serializer for Artist creation.
    '''
    username = serializers.SlugRelatedField(read_only=True,slug_field='name')
    class Meta:
        model = Artist
        #fields = "__all__"
        fields = ["id", "artist_name", "username", "country", "artist_image", "style", "introduction", "quote"]
          
        '''
        #depth = 1
        #the problem here is, the hashed password is also being shown.... lol
        #people recommend to directly use user-serializer instead of depth=1 
        # (which is usually good for "READ ONLY" fields)  --- checked : works perfectly.

        #https://stackoverflow.com/questions/49097981/django-rest-framework-limiting-fields-on-foreignkey-relationship-when-serialize
        '''

class ArtistReadOnlySerializers(serializers.ModelSerializer):
    '''
    serializer for readonly aspects of Artist model.
    '''
    username = serializers.SlugRelatedField(read_only=True,slug_field='name')  #this field by default read-write, u can make it read only by specifying true.
    class Meta:
        model = Artist
        fields = ["id", "artist_name", "username"]


class GallerySerializers(serializers.ModelSerializer):
    '''
    dedicated artist serializer for Artist creation.
    '''
    #g_artist = UserSerializer()
    class Meta:
        model = Gallery
        fields='__all__'
        #fields = ["g_upload-data", "g_datetime", "g_artist"]

        
class GalleryReadOnlySerializers(serializers.ModelSerializer):
    '''
    serializer for readonly aspects of Artist model.
    '''
    g_artist = serializers.SlugRelatedField(read_only=True,slug_field='name')  #this field by default read-write, u can make it read only by specifying true.
    class Meta:
        model = Gallery
        fields = ["id", "g_upload_photo", "g_datetime", "g_artist"]

class WorkSerializers(serializers.ModelSerializer):
    '''
    serializer for work class
    '''

    class Meta:
        model = Work
        fields = "__all__"