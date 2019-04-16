# Generated by Django 2.1.7 on 2019-04-16 08:56

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Название места')),
                ('text', ckeditor.fields.RichTextField(default=None, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата')),
                ('img', models.ImageField(upload_to='')),
            ],
            options={
                'verbose_name': 'Место',
                'verbose_name_plural': 'Места',
            },
        ),
    ]