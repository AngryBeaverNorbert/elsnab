# -*- coding: utf-8 -*-
from django.db import models


class Feedback(models.Model):
    subject = models.CharField(verbose_name=u'Тема', max_length=250, blank=False)
    sender = models.EmailField(verbose_name=u'Відправник', blank=False)
    message = models.TextField(verbose_name=u'Повідомлення', blank=False)
    copy = models.BooleanField(verbose_name=u'Копія', default=False,
                               help_text=u'Виберіть для отримання копії запиту на Вашу пошту')

    def __str__(self):
        return self.sender
