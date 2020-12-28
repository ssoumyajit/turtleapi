
from django.shortcuts import render
from myhood.models import MyHood, Students, Post
from rest_framework import viewsets
from myhood.serializers import MyHoodSerializers, StudentsSerializers, PostSerializers
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

class MyHoodViewSets(viewsets.ModelViewSet):
    queryset = MyHood.objects.all()
    serializer_class = MyHoodSerializers
    lookup_field = "myhood"
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
class StudentsViewSets(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
