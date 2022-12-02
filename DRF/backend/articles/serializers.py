from .models import Article, Pick, Comment
from rest_framework import serializers


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class PickSerializers(serializers.ModelSerializer):
    class Meta:
        model = Pick
        fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
