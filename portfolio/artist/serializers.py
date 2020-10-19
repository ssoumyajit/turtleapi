from rest_framework import serializers
from artist.models import Artist
from user.serializers import UserSerializer
class ArtistSerializers(serializers.ModelSerializer):
    '''
    dedicated artist serializer for Artist creation.
    '''
    username = UserSerializer(many = True,read_only = True)
    class Meta:
        model = Artist
        fields = ['id','artist_name', 'username']
        
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
        #depth = 1