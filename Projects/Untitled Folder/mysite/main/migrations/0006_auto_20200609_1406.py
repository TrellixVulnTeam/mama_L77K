# Generated by Django 3.0.7 on 2020-06-09 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200609_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialseries',
            name='video_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='archive',
            name='archive_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 14, 6, 24, 559794), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 9, 14, 6, 24, 559212), verbose_name='date published'),
        ),
    ]