# Generated by Django 2.1.7 on 2019-04-16 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placestogo', '0002_place_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='img',
        ),
        migrations.AddField(
            model_name='place',
            name='img_url',
            field=models.URLField(default='https://img4.goodfon.ru/original/1920x1408/5/61/norway-mountains-valley-peaks-snow-house-meadow-grass-trees.jpg', verbose_name='URL изображения'),
        ),
    ]
