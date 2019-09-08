from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField("商品名", max_length=128, null=False, blank=False, unique=True)
    # 单位：分
    current_price = models.IntegerField(verbose_name="现价", blank=False, null=False)
    # 单位：分
    origin_price = models.IntegerField(verbose_name="原价", blank=False, null=False)
    banner_display = models.BooleanField(verbose_name="是否展示在 banner 位")

    is_available = models.BooleanField(verbose_name="商品是否有效")
    is_published = models.BooleanField(verbose_name="商品是否已发布")
    unavailable_reason = models.CharField("商品无效原因", max_length=128)

    source = models.CharField("商品来源", max_length=56)
    preface = models.CharField("简介", max_length=256)
    body = models.TextField("内容", null=False)

    thumbnail_url = models.URLField(verbose_name="缩略图链接", max_length=128, blank=False, null=False)
    purchase_url = models.URLField(verbose_name="购买链接", max_length=128, blank=False, null=False)

    def __str__(self):
        return self.name
