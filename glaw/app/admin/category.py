from django.contrib import admin

from ..models import category


@admin.register(category.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = [
        'name',
    ]

    list_filter = [
    ]
