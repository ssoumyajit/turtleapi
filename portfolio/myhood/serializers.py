from rest_framework import serializers
from myhood.models import MyHood, Students, Post
from user.serializers import UserSerializer
from user.models import User

class MyHoodSerializers(serializers.ModelSerializer):
    class Meta:
        model = MyHood
        fields = '__all__'
        depth=1
class StudentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'
        depth=1
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        depth=1