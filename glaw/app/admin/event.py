from django.contrib import admin

from app.models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'is_available',
        'is_published',
    ]
