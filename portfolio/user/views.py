from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView
from .serializers import UserSerializer, AuthTokenSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
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

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})
        #return Response({'token': token.key, 'id': token.user_id, 'user': token.user_email})


class ManageUserView(RetrieveUpdateAPIView):
    """
    manage the authenticated user.
    """
    serializer_class = UserSerializer
    authentication_class = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

#https://github.com/encode/django-rest-framework/issues/2414      getting back user data alogn with token