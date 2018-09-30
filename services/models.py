# -*- coding: utf-8 -
from django.urls import reverse
from django.db import models


class Services(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Сервіс'
        verbose_name_plural = u'Сервіси'

    def __str__(self):
        return self.title


class SingleService(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    category = models.CharField(max_length=120, verbose_name=u'Категорія', help_text=u'Може бути пустим',
                                blank=True, null=True)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')
    timestamp = models.DateField(verbose_name=u'Добавлено', auto_now_add=True)

    class Meta:
        verbose_name        = u'Сервіс (детальний)'
        verbose_name_plural = u'Сервіси (детальні)'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:single-service', kwargs={'pk': self.pk})


def service_upload_location(instance, filename):
    return 'services/service/%s' % filename


class ServiceImage(models.Model):
    service = models.ForeignKey(SingleService, on_delete=models.CASCADE, related_name='service_images')
    image   = models.ImageField(upload_to=service_upload_location)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.service.title


class Montages(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Монтаж'
        verbose_name_plural = u'Монтажі'

    def __str__(self):
        return self.title


class SingleMontage(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    category = models.CharField(max_length=120, verbose_name=u'Категорія', help_text=u'Може бути пустим',
                                blank=True, null=True)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')
    timestamp = models.DateField(verbose_name=u'Добавлено', auto_now_add=True)

    class Meta:
        verbose_name        = u'Монтаж (детальний)'
        verbose_name_plural = u'Монтажі (детальні)'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:single-montage', kwargs={'pk': self.pk})


def montage_upload_location(instance, filename):
    return 'services/montage/%s' % filename


class MontageImage(models.Model):
    service = models.ForeignKey(SingleMontage, on_delete=models.CASCADE, related_name='montage_images')
    image   = models.ImageField(upload_to=montage_upload_location)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.service.title


class Installations(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Інсталяція'
        verbose_name_plural = u'Інсталяції'

    def __str__(self):
        return self.title


class SingleInstallation(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    category = models.CharField(max_length=120, verbose_name=u'Категорія', help_text=u'Може бути пустим',
                                blank=True, null=True)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')
    timestamp = models.DateField(verbose_name=u'Добавлено', auto_now_add=True)

    class Meta:
        verbose_name        = u'Інсталяція (детальна)'
        verbose_name_plural = u'Інсталяції (детальні)'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('services:single-installation', kwargs={'pk': self.pk})


def installation_upload_location(instance, filename):
    return 'services/%s' % filename


class InstallationImage(models.Model):
    service = models.ForeignKey(SingleInstallation, on_delete=models.CASCADE, related_name='installation_images')
    image   = models.ImageField(upload_to=installation_upload_location)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.service.title
