# Generated by Django 2.2.5 on 2019-09-23 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20190923_1421'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='活动名')),
                ('place', models.CharField(max_length=128, verbose_name='活动场地')),
                ('register_start_date', models.DateField(verbose_name='注册开始时间')),
                ('register_end_date', models.DateField(verbose_name='注册结束时间')),
                ('register_url', models.URLField(verbose_name='注册链接')),
                ('start_date', models.DateField(verbose_name='活动开始时间')),
                ('end_date', models.DateField(verbose_name='活动结束时间')),
                ('is_available', models.BooleanField(default=True, verbose_name='是否有效')),
                ('is_published', models.BooleanField(default=False, verbose_name='是否已发布')),
                ('unavailable_reason', models.CharField(blank=True, max_length=128, null=True, verbose_name='无效原因')),
                ('event_pic', models.URLField(blank=True, max_length=128, null=True, verbose_name='活动封面图')),
            ],
            options={
                'verbose_name': '活动',
                'verbose_name_plural': '活动',
            },
        ),
    ]
