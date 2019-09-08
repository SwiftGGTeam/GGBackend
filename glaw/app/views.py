from django.shortcuts import render
from app.serializers.post import PostListSerializer, PostSerializer
from app.models import Post
from app.service.post import index as post_index

from rest_framework import viewsets, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, parser_classes

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

    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post, many=False)
        resp_data = serializer.data
        return Response(render_success(resp_data), status=status.HTTP_200_OK)
    except Post.DoesNotExist:
        return Response(render_failure('没有找到相关文章'), status=status.HTTP_200_OK)

    return Response(render_failure('404 Not Found'), status=status.HTTP_404_NOT_FOUND)


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
