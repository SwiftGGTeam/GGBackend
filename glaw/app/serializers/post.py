from app.models import Post
from rest_framework import serializers, viewsets


class PostListSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False)
    publishDate = serializers.DateTimeField(source='published_at', format="%Y-%m-%d")
    imageURL = serializers.URLField(source='thumbnail')

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'preface',
            'imageURL',
            'category',
            'publishDate'
        )


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
        )
