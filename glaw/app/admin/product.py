from django.contrib import admin

from app.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'current_price',
        'origin_price',
        'banner_display',
        'is_available',
        'is_published',
        'unavailable_reason',
        'source',
        'preface',
        'body',
        'thumbnail_url',
        'purchase_url'
    ]
