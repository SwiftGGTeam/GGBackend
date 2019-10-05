from app.serializers.post import PostListSerializer, PostSerializer

from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes

from django.core.paginator import Paginator

from app.views import render
from app.models import Post, PageBean


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@parser_classes((JSONParser,))
def post_list(request):
    try:
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('size', 10))
    except ValueError:
        return render.parameters_illegal()

    all_posts = Post.objects.all().order_by('-published_at')
    total = len(all_posts)
    paginator = Paginator(all_posts, limit)
    page_bean = PageBean(page, limit, total)

    if paginator.num_pages < page:
        return render.page_success(page_bean, [])

    posts = paginator.page(page)
    serializer = PostListSerializer(posts, many=True)
    return render.page_success(page_bean, serializer.data)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
@parser_classes((JSONParser,))
def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        return render.failure('没有找到相关文章')

    serializer = PostSerializer(post, many=False)
    return render.success(serializer.data)
