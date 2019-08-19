from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField("标签名", max_length=128, null=False, blank=False, unique=True)
    color = models.IntegerField("标签颜色")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

        index_together = [
            ['color'],
        ]
