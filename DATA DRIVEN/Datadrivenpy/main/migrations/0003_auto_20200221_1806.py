# Generated by Django 3.0.3 on 2020-02-21 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200221_1759'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ('-tutorial_published',)},
        ),
    ]