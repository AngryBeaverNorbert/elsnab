# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class Home(models.Model):
    title  = models.CharField(max_length=254, verbose_name=u'Заголовок', blank=False)
    body   = models.TextField(verbose_name=u'Тіло')
    active = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                 help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name = u'Домашня сторінка'
        verbose_name_plural = u'Домашні сторінки'

    def __str__(self):
        return self.title
