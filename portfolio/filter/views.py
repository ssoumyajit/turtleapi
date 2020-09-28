from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView
from .serializers import ArtistSerializer, GallerySerializer
from .models import Artist, Gallery
from rest_framework import filters


class CreateArtistView(CreateAPIView):
    serializer_class = ArtistSerializer

class ListArtistView(ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['artist']


class CreateGalleryView(CreateAPIView):
    serializer_class = GallerySerializer

class ListGalleryView(ListAPIView):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['artist__artist']


#filter_fields = ('g_artist',)
class ArtistFilteredView(ListAPIView):
    serializer_class = ArtistSerializer
    filter_fields = ('artist',)

    def get_queryset(self):
        """
        This view should return a list of all gallery photos,
        for the artist as determined by the artist name.
        """
        artist = self.kwargs['artist']
        return Artist.objects.filter(artist__artist = artist)







