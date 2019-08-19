from django.contrib import admin

from ..models import tag


@admin.register(tag.Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'color',
    ]