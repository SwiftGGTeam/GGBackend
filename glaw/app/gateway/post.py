from app.serializers.post import PostSerializer
from app.models import Post
from app.service.post import index as post_index

from rest_framework import viewsets, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, parser_classes


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def query_posts(request):
    if request.method == 'GET':
        page = request.GET.get('page', 1)
        limit = request.GET.get('limit', 20)
        posts, total = post_index(page=page, limit=limit)
        serializer = PostSerializer(posts, many=True)
        resp_data = {
            'page': page,
            'page_size': limit,
            'total': total,
            'detail': serializer.data,
        }
        return Response(resp_data, status=status.HTTP_200_OK)




