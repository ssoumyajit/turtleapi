from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .serializers import UserSerializer, AuthTokenSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from rest_framework import generics, authentication, permissions

class CreateUserView(CreateAPIView):
    """create a new user in the system"""
    serializer_class  = UserSerializer
    
class CreateTokenView(ObtainAuthToken):
    """
    create a new auth token for the user.
    """

    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(RetrieveUpdateAPIView):
    """
    manage the authenticated user.
    """
    serializer_class = UserSerializer
    authentication_class = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user