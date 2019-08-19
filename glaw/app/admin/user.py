from django.contrib import admin

from app.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        'nickname',
        'intro_url',
        'blog_url',
        'weibo_url',
        'github_url',
    ]

