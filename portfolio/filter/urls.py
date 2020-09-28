from django.urls import path
from rest_framework import generics
from .views import CreateArtistView, CreateGalleryView, \
                   ListArtistView, ListGalleryView, ArtistFilteredView
from .serializers import ArtistSerializer, GallerySerializer

app_name = 'filter'

urlpatterns = [
    path('artist/create/', CreateArtistView.as_view(), name = 'artist_creation'),    
    path('gallery/create/', CreateGalleryView.as_view(), name = 'gallery_creation'),
    path('artist/', ListArtistView.as_view(), name = 'list_artists'),
    path('gallery/', ListGalleryView.as_view(), name = 'list_galleries'),
    path('api/v1/filter/artist/(?P<username>.+)/$', ArtistFilteredView.as_view(), name='artist_filtered'),
]

#{'get': 'list'}