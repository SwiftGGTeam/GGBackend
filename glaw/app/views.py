from django.shortcuts import render
from app.serializers.post import PostListSerializer, PostSerializer
from app.serializers.product import ProductListSerializer, ProductSerializer
from app.models import Post, Product
from app.service.post import index as post_index

from rest_framework import viewsets, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, parser_classes

# from app.core import post_crawl

# Create your views here.


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def query_posts(request):
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('size', 10))

    posts, total = post_index(page=page, limit=limit)
    serializer = PostListSerializer(posts, many=True)

    resp_data = render_page_resp(page, limit, total, serializer.data)
    return Response(render_success(resp_data), status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def query_post(request, post_id):
    if request.method != 'GET':
        return Response(render_failure('Method Not Allowed'), status=status.HTTP_405_METHOD_NOT_ALLOWED)

    res_data = render_failure('404 Not Found')
    res_status = status.HTTP_404_NOT_FOUND
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, many=False)
        res_data = render_success(serializer.data)
        res_status = status.HTTP_200_OK
    except Post.DoesNotExist:
        res_data = render_failure('没有找到相关文章')
        res_status = status.HTTP_200_OK
    finally:
        return Response(res_data, status=res_status)


# @api_view(['GET'])
# @permission_classes((permissions.AllowAny, ))
# @parser_classes((JSONParser,))
# def crawl_post(request):
#     res = post_crawl.executor_post()
#     post_crawl.bulk_update(res)
#     return Response(render_success(res), status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def query_products(request):
    if request.method != 'GET':
        return Response(render_failure('Method Not Allowed'), status=status.HTTP_405_METHOD_NOT_ALLOWED)

    banner_products = ProductListSerializer(
        Product.objects.all().filter(banner_display=True).order_by('-id'), many=True
    ).data
    list_products = ProductListSerializer(
        Product.objects.all().filter(banner_display=False).order_by('-id'), many=True
    ).data
    data = {
        'banner': banner_products,
        'list': list_products
    }
    return Response(render_success(data), status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def query_product(request, product_id):
    if request.method != 'GET':
        return Response(render_failure('Method Not Allowed'), status=status.HTTP_405_METHOD_NOT_ALLOWED)

    res_data = render_failure('404 Not Found')
    res_status = status.HTTP_404_NOT_FOUND
    try:
        product = Product.objects.get(id=product_id)
        serializer = ProductSerializer(product, many=False)
        res_data = render_success(serializer.data)
        res_status = status.HTTP_200_OK
    except Product.DoesNotExist:
        res_data = render_failure('没有找到相关商品')
        res_status = status.HTTP_200_OK
    finally:
        return Response(res_data, status=res_status)


def render_page_resp(page, limit, total, items):
    return {
        'pageBean': {
            'page': page,
            'size': limit,
            'total': total,
        },
        'items': items,
    }


def render_success(data):
    return {
        'success': True,
        'message': '',
        'results': data
    }


def render_failure(reason):
    return {
        'success': False,
        'message': reason,
        'results': None
    }
