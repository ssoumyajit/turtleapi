from rest_framework.serializers import ModelSerializer
from filter.models import Artist, Gallery

class ArtistSerializer(ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"
        
class GallerySerializer(ModelSerializer):
    
    class Meta:
        model = Gallery
        fields = "__all__"
    
