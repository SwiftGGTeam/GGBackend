from app.models import Category
from rest_framework import serializers, viewsets


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )

