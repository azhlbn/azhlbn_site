# Generated by Django 2.1.7 on 2019-04-16 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placestogo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='slug',
            field=models.SlugField(default=None, verbose_name='URL'),
        ),
    ]
