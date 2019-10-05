from django.urls import re_path

from app.views import post, product, event

urlpatterns = [
    re_path(r'^posts$', post.post_list),
    re_path(r'^post/(?P<post_id>\d+)$', post.post_detail),

    re_path(r'products$', product.product_list),
    re_path(r'product/(?P<product_id>\d+)$', product.product_detail),

    re_path(r'events$', event.event_list)
]
