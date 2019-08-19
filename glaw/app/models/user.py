from django.db import models


class User(models.Model):
    nickname = models.CharField("昵称", max_length=128, unique=True)
    intro_url = models.URLField("个人链接", max_length=255, null=True, blank=True)
    avatar_url = models.URLField("头像", max_length=255, null=True, blank=True)

    blog_url = models.URLField("博客链接", max_length=255, null=True, blank=True)
    weibo_url = models.URLField("微博链接", max_length=255, null=True, blank=True)
    github_url = models.URLField("GitHub 链接", max_length=255, null=True, blank=True)
    twitter_url = models.URLField("Twitter", max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = '成员'
        verbose_name_plural = verbose_name

        index_together = []
