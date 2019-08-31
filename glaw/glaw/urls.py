"""glaw URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from app.gateway import post as glaw_post
from app.gateway import base as glaw_base

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include(('app.urls', 'app'), namespace='app'))
    # path('', include('app.urls')),
]

# app_urlpatterns = [
#     path(glaw_base.url_prefix('posts'), glaw_post.query_posts),
#     # path(glaw_base.url_prefix('post_spider'), glaw_post.posts_spider),
# ]

# urlpatterns += app_urlpatterns
