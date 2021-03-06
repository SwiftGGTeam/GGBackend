from django.db import models


# Create your models here.
class Event(models.Model):
    name = models.CharField("活动名", max_length=128, null=False, blank=False, unique=True)
    place = models.CharField("活动场地", max_length=128, null=False, blank=False)

    register_start_date = models.DateField("注册开始时间", null=False, blank=False)
    register_end_date = models.DateField("注册结束时间", null=False, blank=False)
    register_url = models.URLField("注册链接", null=False, blank=False)

    start_date = models.DateField("活动开始时间", null=False, blank=False)
    end_date = models.DateField("活动结束时间", null=False, blank=False)

    is_available = models.BooleanField(verbose_name="是否有效", default=True)
    is_published = models.BooleanField(verbose_name="是否已发布", default=False)
    unavailable_reason = models.CharField("无效原因", max_length=128, blank=True, null=True)

    event_pic = models.URLField(verbose_name="活动封面图", max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = verbose_name

        index_together = []
