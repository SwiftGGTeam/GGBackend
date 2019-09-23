from app.models import Event

from django.core.paginator import Paginator


def index(page=1, limit=20):
    """
    分页活动
    :param page:
    :param limit:
    :return:
    """
    events = Event.objects.all().order_by('-register_end_date')
    tot = len(events)
    paginator = Paginator(events, limit)
    if paginator.num_pages < page:
        return [], tot
    result = paginator.page(page)
    return list(result), tot
