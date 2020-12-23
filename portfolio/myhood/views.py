
from django.shortcuts import render
from myhood.models import MyHood, Students, Post
from rest_framework import viewsets
from myhood.serializers import MyHoodSerializers, StudentsSerializers, PostSerializers
from rest_framework import filters

class MyHoodViewSets(viewsets.ModelViewSet):
    queryset = MyHood.objects.all()
    serializer_class = MyHoodSerializers
    lookup_field = "myhood"
class StudentsViewSets(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializers
class PostViewSets(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
