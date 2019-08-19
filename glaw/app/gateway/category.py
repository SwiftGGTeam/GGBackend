from app.serializers.category import CategorySerializer
from app.models import Category

from rest_framework import viewsets, status, permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action, api_view, permission_classes, parser_classes


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny, ))
@parser_classes((JSONParser,))
def query_categories(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
