from rest_framework import serializers
from .models import Sharing, Comments, LikesToSharing, OneReasonVid, OneRememberVid, LearningsVid
# from user.serializers import UserSerializer
from user.models import User


class LikesToSharingSerializers(serializers.ModelSerializer):

    l_liker = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = LikesToSharing
        fields = ['id', 'l_shareid', 'l_liker', 'l_type']


class CommentSerializers(serializers.ModelSerializer):
    c_commenter = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='name')

    class Meta:
        model = Comments
        fields = ['id', 'c_shareid', 'c_commenter', 'c_comment']


class SharingSerializers(serializers.ModelSerializer):
    s_student = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    s_teacher = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    # likes_count = serializers.SerializerMethodField()
    likes_sharing = LikesToSharingSerializers(many = True, read_only = True)
    comments_sharing = CommentSerializers(many = True, read_only = True)

    class Meta:
        model = Sharing
        fields = ['id', 's_student', 's_teacher', 's_teacher_name', 's_photo', 's_appreciation',
                  's_date', 's_location', 'likes_sharing', 'comments_sharing']

    # def get_likes_count(self, instance):
    # to do this u have to use serializermethodfield, confirm once.
    # return instance.voters_like.count()


class OneReasonVidSerializers(serializers.ModelSerializer):

    class Meta:
        model = Sharing
        fields = "__all__"


class OneRememberVidSerializers(serializers.ModelSerializer):

    class Meta:
        models = Sharing
        fields = "__all__"


class LearningsVideSerializers(serializers.ModelSerializer):

    class Meta:
        models = LearningsVid
        fields = "__all__"
