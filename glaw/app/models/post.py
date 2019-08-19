from django.db import models

from app.models.tag import Tag
from app.models.user import User
from app.models.category import Category


# Create your models here.
class Post(models.Model):
    title = models.CharField("文章标题", max_length=128, null=False, blank=False, unique=True)
    origin_title = models.CharField("原文标题", max_length=128, null=True, blank=True, unique=True)
    body = models.TextField("内容")

    # 原文作者
    author = models.CharField(verbose_name="作者", max_length=128)
    # 译者（可能多人）
    translators = models.ManyToManyField(User, related_name="translators", verbose_name="译者")
    # 校对者（可能多人）
    proofreaders = models.ManyToManyField(User, related_name="proofreaders", verbose_name="校对者")
    # 定稿人
    drafters = models.ManyToManyField(User, related_name="drafters", verbose_name="定稿人")
    # 原文链接
    html_url = models.URLField(verbose_name="原文链接", max_length=128, blank=True, null=True)
    # GitHub 链接
    github_url = models.URLField(verbose_name="GitHub 链接", max_length=128, blank=True, null=True)

    tag = models.ManyToManyField(Tag, related_name="tags", verbose_name="标签")
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL, verbose_name="分类")

    created_at = models.DateTimeField("创建时间", auto_now_add=True)
    updated_at = models.DateTimeField("上次修改时间", auto_now=True)
    published_at = models.DateTimeField("译文发布时间", auto_now_add=True)
    origin_at = models.DateTimeField("原文创建时间", auto_now=True)

    def __str__(self):
        s = "{title} - {author}, {date}"
        return s.format(title=self.title, author=self.author, date=str(self.created_at))

    class Meta:
        verbose_name = '博文'
        verbose_name_plural = verbose_name

        unique_together = (
            ('title', 'author'),
        )

        index_together = [
            ['title'],
        ]
