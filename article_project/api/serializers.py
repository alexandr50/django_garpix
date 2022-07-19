from rest_framework import serializers
from article.models import Article, Comments
from drf_writable_nested import WritableNestedModelSerializer

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('header', 'text')

class CommentSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    name_art = ArticleSerializer()

    class Meta:

        model = Comments
        fields = '__all__'