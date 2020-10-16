from rest_framework.serializers import ModelSerializer
from artist.models import Artist

class ArtistSerializers(ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"