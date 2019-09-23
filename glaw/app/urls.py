from django.urls import path, re_path
from django.conf.urls import url

from app.gateway import post as glaw_post
from . import views

urlpatterns = [
    re_path(r'^app/posts$', views.query_posts),
    re_path(r'^app/post/(?P<post_id>\d+)$', views.query_post),
    # re_path(r'^crawl/posts$', views.crawl_post)

    re_path(r'app/products$', views.query_products),
    re_path(r'app/product/(?P<product_id>\d+)$', views.query_product),

    re_path(r'app/events$', views.query_events)
]
