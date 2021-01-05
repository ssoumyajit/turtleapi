from rest_framework import serializers
from artist.models import Bio, Artist, Gallery, Highlights, Events, JudgingWorkshop
from user.serializers import UserSerializer
from user.models import User

class ArtistSerializers(serializers.ModelSerializer):

    #overridden username here
    username = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name') # this is where the bug is, so don can patch on batalla while updating in postman
    class Meta:
        model = Artist
        fields = ['username','artist_name', 'cover', 'thumb', 'country']
    
    def __init__(self, *args, **kwargs):
        
        #don't return covers when listing artists
        if kwargs['context']['view'].action == 'list':
            del self.fields['cover']
        
        super().__init__(*args, **kwargs)
    
class BioSerializers(serializers.ModelSerializer):
    '''
    dedicated artist serializer for Artist creation.
    '''
    b_artist = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    class Meta:
        model = Bio
        fields = "__all__"
          
        '''
        #depth = 1
        #the problem here is, the hashed password is also being shown.... lol
        #people recommend to directly use user-serializer instead of depth=1 
        # (which is usually good for "READ ONLY" fields)  --- checked : works perfectly.

        #https://stackoverflow.com/questions/49097981/django-rest-framework-limiting-fields-on-foreignkey-relationship-when-serialize
        '''

#------
#g_artist = UserSerializer()
#------

class GallerySerializers(serializers.ModelSerializer):
    '''
    dedicated artist serializer for Artist creation.
    '''
    g_artist = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    class Meta:
        model = Gallery
        fields='__all__'  #i think it should be double quotes, but docs says single quote is right.

        
class HighlightsSerializers(serializers.ModelSerializer):
    '''
    serializer for work class
    '''
    h_artist = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    class Meta:
        model = Highlights
        fields = "__all__"


class JudgingWorkshopSerializers(serializers.ModelSerializer):
    jw_artist = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    class Meta:
        model = JudgingWorkshop
        fields = "__all__"


class EventsSerializers(serializers.ModelSerializer):
    ev_artist = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    class Meta:
        model = Events
        fields = "__all__"


        
#------------------------------------------------------------
class ArtistReadOnlySerializers(serializers.ModelSerializer):
    '''
    serializer for readonly aspects of Artist model.
    '''
    username = serializers.SlugRelatedField(read_only=True,slug_field='name')  #this field by default read-write, u can make it read only by specifying true.
    class Meta:
        model = Artist
        fields = ["id", "artist_name", "username"]

class GalleryReadOnlySerializers(serializers.ModelSerializer):
    '''
    serializer for readonly aspects of Artist model.
    '''
    g_artist = serializers.SlugRelatedField(read_only=True,slug_field='name')  #this field by default read-write, u can make it read only by specifying true.
    class Meta:
        model = Gallery
        fields = ["id", "g_upload_photo", "g_datetime", "g_artist"]