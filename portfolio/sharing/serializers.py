from rest_framework import serializers
from sharing.models import Sharing, Comments
#from user.serializers import UserSerializer
from user.models import User


class CommentSerializers(serializers.ModelSerializer):
    commenter = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    class Meta:
        model = Comments
        fields = ['shareid', 'commenter', 'comment']


class SharingSerializers(serializers.ModelSerializer):
    s_student = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    s_teacher = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    likes_count = serializers.SerializerMethodField()
    comment = CommentSerializers(many = True, read_only = True)
    class Meta:
        model = Sharing
        fields = ['id', 's_student', 's_teacher', 's_teacher_name', 's_photo', 's_appreciation', 's_video_talk',
                 's_video_dance', 's_date', 's_location', 'likes_count', 'comment']
        #exclude = ["voters_like"]
        #fields = ['s_student', 's_teacher', '']

    def get_likes_count(self, instance):
        return instance.voters_like.count()