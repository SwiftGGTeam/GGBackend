from app.models import Post

from django.core.paginator import Paginator


def index(page=1, limit=20):
    """
    分页文章
    :param page:
    :param limit:
    :return:
    """
    posts = Post.objects.all().order_by('-published_at')
    tot = len(posts)
    paginator = Paginator(posts, limit)
    result = paginator.page(page)
    return list(result), tot

