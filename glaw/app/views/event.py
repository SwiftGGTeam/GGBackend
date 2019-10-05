from app.serializers.event import EventListSerializer

from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes, parser_classes

from django.core.paginator import Paginator

from app.views import render
from app.models import Event, PageBean


@api_view(['GET'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def event_list(request):
    try:
        page = int(request.GET.get('page', 1))
        limit = int(request.GET.get('size', 10))
    except ValueError:
        return render.parameters_illegal()

    all_events = Event.objects.all().order_by('-register_end_date').filter(is_available=True)
    total = len(all_events)
    paginator = Paginator(all_events, limit)
    page_bean = PageBean(page, limit, total)

    if paginator.num_pages < page:
        return render.page_success(page_bean, [])

    events = paginator.page(page)

    serializer = EventListSerializer(events, many=True)
    return render.page_success(page_bean, serializer.data)
