from app.models import Event
from rest_framework import serializers

from datetime import datetime


class EventListSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    imageURL = serializers.URLField(source='event_pic')
    registerURL = serializers.URLField(source='register_url')

    class Meta:
        model = Event
        fields = (
            'name',
            'state',
            'date',
            'place',
            'imageURL',
            'registerURL'
        )

    def get_state(self, obj):
        return "开放报名中"

    def get_date(self, obj):
        return obj.start_date.strftime('%Y-%m-%d') + ' ~ ' + obj.end_date.strftime('%Y-%m-%d')
