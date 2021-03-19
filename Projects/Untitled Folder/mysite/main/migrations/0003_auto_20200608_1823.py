# Generated by Django 3.0.7 on 2020-06-08 15:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200608_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archive',
            name='archive_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 18, 23, 37, 147736), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='tutorial',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='main.TutorialSeries'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 8, 18, 23, 37, 145491), verbose_name='date published'),
        ),
    ]