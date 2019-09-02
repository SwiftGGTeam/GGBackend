from django.urls import path
from django.conf.urls import url

from app.gateway import post as glaw_post
from . import views

urlpatterns = [
    url(r'^app/posts$', views.query_posts, name='posts'),
    url(r'^app/post$', views.query_post, name='post')
]
