from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField("商品名", max_length=128, null=False, blank=False, unique=True)
    # 单位：分
    current_price = models.IntegerField(verbose_name="现价", blank=False, null=False)
    # 单位：分
    origin_price = models.IntegerField(verbose_name="原价", blank=False, null=False)
    banner_display = models.BooleanField(verbose_name="是否展示在 banner 位")

    is_available = models.BooleanField(verbose_name="商品是否有效", default=True)
    is_published = models.BooleanField(verbose_name="商品是否已发布", default=False)
    unavailable_reason = models.CharField("商品无效原因", max_length=128, blank=True, null=True)

    source = models.CharField("商品来源", max_length=56, blank=True, null=True)
    preface = models.CharField("简介", max_length=256, blank=True, null=True)
    body = models.TextField("内容")

    thumbnail_url = models.URLField(verbose_name="缩略图链接", max_length=128, blank=False, null=False)
    purchase_url = models.URLField(verbose_name="购买链接", max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

        index_together = [
            ['name'],
        ]
