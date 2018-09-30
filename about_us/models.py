# -*- coding: utf-8 -*-
from django.db import models


def upload_location(instance, filename):
    return 'about_us/%s' % filename


class AboutUs(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Заголовок', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    image   = models.ImageField(verbose_name=u'Зображення', blank=False, upload_to=upload_location)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name = u'Про нас'
        verbose_name_plural = u'Про нас'

    def __str__(self):
        return self.title
