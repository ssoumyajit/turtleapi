from django.contrib.auth import get_user_model, authenticate
from rest_framework.serializers import ModelSerializer
from .models import User
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

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

    def update(self, instance, validated_data):
        """
        update a user, setting the password correctly and return it.
        """
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
        

class AuthTokenSerializer(serializers.Serializer):
    """
    serializer for user authentication object.
    """

    email = serializers.CharField()
    password = serializers.CharField(
        style = {'input_type': 'password'},
        trim_whitespace = False
    )

    def validate(self, attrs):
        """
        validate and authenticate the user
        """

        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(
            request = self.context.get('request'),
            username = email,
            password = password
        )
        if not user:
            msg = _('unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code = 'authorization')

        attrs['user'] = user
        return attrs
        #you always return the object at the end of the validation.


