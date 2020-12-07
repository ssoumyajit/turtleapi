from django.shortcuts import render
from .models import Artist, Work, Gallery
from rest_framework import viewsets
from artist.serializers import ArtistSerializers, ArtistReadOnlySerializers, GallerySerializers, WorkSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import mixins
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication

class ArtistViewSets(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    lookup_field = "username__name"
    filter_backends = [filters.SearchFilter]
    search_fields = ['username__name']

    #authentication_classes = (TokenAuthentication,)
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class GalleryViewSets(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['g_artist__name']
    
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class WorkViewSets(viewsets.ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['w_artist__name']

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)