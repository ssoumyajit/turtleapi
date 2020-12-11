from rest_framework import serializers
from sharing.models import Sharing
#from user.serializers import UserSerializer
from user.models import User

class SharingSerializers(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    class Meta:
        model = Sharing
        exclude = ["voters_like"]
        #fields = ['s_student', 's_teacher', '']

    def get_likes_count(self, instance):
        return instance.voters_like.count()
