from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Artist
from rest_framework import viewsets
from artist.serializers import ArtistSerializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CreateArtistView(CreateAPIView):
    """
    create a new Artist Portfolio.
    """
    serializer_class = ArtistSerializers
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    pass


class ArtistView(viewsets.ModelViewSet):
    serializer_class = ArtistSerializers
    queryset = Artist.objects.all()