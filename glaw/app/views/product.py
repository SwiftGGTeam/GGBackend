from app.serializers.product import ProductListSerializer, ProductSerializer

from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes

from app.views import render
from app.models import Product


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def product_list(request):
    banner_products = ProductListSerializer(
        Product.objects.all().filter(banner_display=True, is_available=True).order_by('-id'), many=True
    ).data
    list_products = ProductListSerializer(
        Product.objects.all().filter(banner_display=False, is_available=True).order_by('-id'), many=True
    ).data
    result = {
        'banner': banner_products,
        'list': list_products
    }
    return render.success(result)


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def product_detail(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render.failure('没有找到相关商品')

    serializer = ProductSerializer(product, many=False)
    return render.success(serializer.data)
