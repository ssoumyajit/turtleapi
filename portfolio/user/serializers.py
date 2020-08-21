from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):
    """ serializer for users object"""

    class Meta:
        model = get_user_model() #return the use model that is active in this project
        #model = User
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}
        
    def create(self, validated_data):
        """create a new user with encrypted password and return it"""
        """basically overwrites the create function provided by base user class \
           and uses our custom user model"""
        return get_user_model().objects.create_user(**validated_data)
        