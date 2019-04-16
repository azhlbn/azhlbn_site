from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Place(models.Model):
    title = models.CharField(max_length=40, verbose_name='Название места')
    slug = models.SlugField(verbose_name='URL', default=None)
    text = RichTextField(default=None, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    # img = models.ImageField()
    img_url = models.URLField(default='https://img4.goodfon.ru/original/1920x1408/5/61/norway-mountains-valley-peaks-snow-house-meadow-grass-trees.jpg', verbose_name='URL изображения')

    def __str__(self):
        return self.title

    def snippet(self):
        return self.text[:200] + '...'

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

