from django.db import models


class Category(models.Model):
    name = models.CharField("分类", max_length=128, null=False, blank=False, unique=True)

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        s = "{name}"
        return s.format(name=self.name)
