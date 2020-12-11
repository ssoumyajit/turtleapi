from django.shortcuts import render
from .models import Artist, Work, Gallery
from rest_framework import viewsets
from artist.serializers import ArtistSerializers, ArtistReadOnlySerializers, GallerySerializers, WorkSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import mixins
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication

#read & retrieve using "username", create & update using "id"

class ArtistViewSets(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    #lookup_field = "username__name"     #previously we were using it for update
    #but let's keep it uniform and use the "id" for update from UI. now we require ?search=username option.
    filter_backends = [filters.SearchFilter]
    search_fields = ['username__name']

    #authentication_classes = (TokenAuthentication,)
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class GalleryViewSets(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
    #lookup_field = "g_artist__name"     #we won't use it here, coz, multiple instances available
    #which cannot be shown under a single URL.
    filter_backends = [filters.SearchFilter]
    search_fields = ['g_artist__name']
    
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class WorkViewSets(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers
    #lookup_field = "username__name"
    filter_backends = [filters.SearchFilter]
    search_fields = ['w_artist__name']

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
