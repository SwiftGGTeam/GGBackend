from app.models import Post
from rest_framework import serializers, viewsets


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = (
            'id',
            'title',
            'body',
            'html_url',
        )
