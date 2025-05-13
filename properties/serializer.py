from rest_framework.serializers import ModelSerializer
from properties.models import Comment


class CommentModelSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ['user', 'property', 'comment']
from rest_framework.serializers import ModelSerializer
from properties.models import Comment

class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['user', 'property','comment']  # Uchta tilni qo‘shish
