from django.shortcuts import render
from .models import Bio, Artist, Highlights, Gallery, Events, JudgingWorkshop
from rest_framework import viewsets
from artist.serializers import  BioSerializers, ArtistSerializers, GallerySerializers, HighlightsSerializers, JudgingWorkshopSerializers, EventsSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import mixins
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication


class ArtistViewSets(viewsets.ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializers
    lookup_field = "username__name"     #previously we were using it for update
    #but let's keep it uniform and use the "id" for update from UI. now we require ?search=username option.
    #filter_backends = [filters.SearchFilter]
    #search_fields = ['username__name']

    #authentication_classes = (TokenAuthentication,)
    #authentication_classes = (JWTAuthentication,)
    #permission_classes = (IsAuthenticatedOrReadOnly,)

class BioViewSets(viewsets.ModelViewSet):
    queryset = Bio.objects.all()
    serializer_class = BioSerializers

class GalleryViewSets(viewsets.ModelViewSet):
    queryset = Gallery.objects.all()
    serializer_class = GallerySerializers
    #lookup_field = "g_artist__name"     #we won't use it here, coz, multiple instances available
    #which cannot be shown under a single URL.
    filter_backends = [filters.SearchFilter]
    search_fields = ['g_artist__name']
    
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class HighlightsViewSets(viewsets.ModelViewSet):
    queryset = Highlights.objects.all()
    serializer_class = HighlightsSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['w_artist__name']

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)


class JudgingWorkshopViewSets(viewsets.ModelViewSet):
    queryset = JudgingWorkshop.objects.all()
    serializer_class = JudgingWorkshopSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['jw_artist__name']

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

class EventsViewSets(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventsSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['ev_artist__name']

    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)

