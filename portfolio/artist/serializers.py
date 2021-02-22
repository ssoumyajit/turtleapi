from rest_framework import serializers
from .models import Artist, ArtistData, Highlights, Journey
from user.models import User
# from portfolio import settings


class ArtistSerializers(serializers.ModelSerializer):

    # overridden username here
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')  # this is where the bug is, so don can patch on Batala while updating in postman
    # owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = Artist
        fields = ['username', 'artist_name', 'cover', 'thumb', 'country']
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
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = ArtistData
        fields = ['username', 'style', 'quote', 'introduction', 'crew', 'ig', 'fb', 'site', 'gallery1', 'gallery2',
                  'gallery2', 'gallery3', 'gallery4']


class HighlightsSerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Highlights
        fields = "__all__"


class JourneySerializers(serializers.ModelSerializer):
    username = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Journey
        fields = "__all__"
# ------------------------------------------------------------


