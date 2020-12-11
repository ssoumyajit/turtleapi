from django.shortcuts import render
from .models import Sharing
from rest_framework import viewsets
from .serializers import SharingSerializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication

class SharingViewSets(viewsets.ModelViewSet):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['s_teacher__name', 's_student__name']

