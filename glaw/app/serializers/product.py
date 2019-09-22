from app.models import Product
from rest_framework import serializers


class ProductListSerializer(serializers.ModelSerializer):
    imageURL = serializers.URLField(source='thumbnail_url')
    price = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'preface',
            'imageURL'
        )

    def get_price(self, obj):
        return obj.current_price / 100.0


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    originPrice = serializers.SerializerMethodField()
    detail = serializers.CharField(source='body')
    purchaseURL = serializers.URLField(source='purchase_url')

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'originPrice',
            'detail',
            'purchaseURL'
        )

    def get_price(self, obj):
        return obj.current_price / 100.0

    def get_originPrice(self, obj):
        return obj.origin_price / 100.0
