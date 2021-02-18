from rest_framework import serializers
from artist.models import Artist, ArtistData, Highlights, Events
from user.models import User
# from portfolio import settings


class ArtistSerializers(serializers.ModelSerializer):

    # overridden username here
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')  # this is where the bug is, so don can patch on Batala while updating in postman
    # owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = Artist
        fields = ['id', 'username', 'artist_name', 'cover', 'thumb', 'country']
        # extra_kwargs = {
        # 'url': {'lookup_field': 'owner'}
        # }

    '''
    def __init__(self, *args, **kwargs):
        
        # don't return covers when listing artists
        if kwargs['context']['view'].action == 'list':
            del self.fields['cover']
        
        super().__init__(*args, **kwargs)
    '''


class ArtistDataSerializers(serializers.ModelSerializer):
    # ownerdata = serializers.ReadOnlyField(source='ownerdata.name')

    class Meta:
        model = ArtistData
        fields = ['id', 'username', 'style', 'quote', 'introduction', 'crew', 'ig', 'fb', 'site', 'gallery1', 'gallery2',
                  'gallery2', 'gallery3', 'gallery4']


class HighlightsSerializers(serializers.ModelSerializer):
    # h_artist = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Highlights
        fields = "__all__"


class EventsSerializers(serializers.ModelSerializer):
    ev_artist = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Events
        fields = "__all__"
# ------------------------------------------------------------


