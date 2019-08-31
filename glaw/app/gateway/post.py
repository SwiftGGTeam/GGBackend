from app.serializers.post import PostListSerializer
from app.models import Post
from app.service.post import index as post_index

from rest_framework import viewsets, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, parser_classes

from app.core import post_crawl


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def query_posts(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('limit', 20))

        posts, total = post_index(page=page, limit=limit)
        serializer = PostListSerializer(posts, many=True)

        resp_data = {
            'pageBean': {
                'page': page,
                'size': limit,
                'total': total,
            },
            'detail': serializer.data,
        }
        return Response(resp_data, status=status.HTTP_200_OK)


# @api_view(['GET'])
# @permission_classes((permissions.AllowAny, ))
# @parser_classes((JSONParser,))
# def posts_spider(request):
#     if request.method == 'GET':
#         ret = post_crawl.excutor_post()
#         post_crawl.bulk_insert(ret)
#         return Response(ret, status=status.HTTP_200_OK)




