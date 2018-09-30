# -*- coding: utf-8 -*-
from django.db import models


class Panels(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Електрощит'
        verbose_name_plural = u'Електрощити'

    def __str__(self):
        return self.title


def panel_upload_location(instance, filename):
    return 'products/panels/%s' % filename


class PanelImage(models.Model):
    panel = models.ForeignKey(Panels, on_delete=models.CASCADE, related_name='panel_images')
    image = models.ImageField(upload_to=panel_upload_location)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.panel.title


class Stabilizers(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Стабілізатор'
        verbose_name_plural = u'Стабілізатори'

    def __str__(self):
        return self.title


def stabilizer_upload_location(instance, filename):
    return 'products/stabilizers/%s' % filename


class StabilizerImage(models.Model):
    stabilizer = models.ForeignKey(Stabilizers, on_delete=models.CASCADE, related_name='stabilizer_images')
    image      = models.ImageField(upload_to=stabilizer_upload_location)
    active     = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                     help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.stabilizer.title


class Ups(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Джерело безперебійного живлення'
        verbose_name_plural = u'Джерела безперебійного живлення'

    def __str__(self):
        return self.title


def ups_upload_location(instance, filename):
    return 'products/ups/%s' % filename


class UpsImage(models.Model):
    ups        = models.ForeignKey(Ups, on_delete=models.CASCADE, related_name='ups_images')
    image      = models.ImageField(upload_to=ups_upload_location)
    active     = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                     help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.ups.title


class Genset(models.Model):
    diesel_image  = models.ImageField(verbose_name=u'Фото дизель-генератора', upload_to='products/genset/diesel',
                                      blank=False)
    diesel_active = models.BooleanField(verbose_name=u'Дизель-генератор', default=True,
                                        help_text=u'Для відображення на сайті необхідно виділити!')
    benzine_image  = models.ImageField(verbose_name=u'Фото бензинового генератора', upload_to='products/genset/benzine',
                                       blank=False)
    benzine_active = models.BooleanField(verbose_name=u'Бензиновий генератор', default=True,
                                         help_text=u'Для відображення на сайті необхідно виділити!')
    gas_image  = models.ImageField(verbose_name=u'Фото газового генератора', upload_to='products/genset/gas',
                                   blank=False)
    gas_active = models.BooleanField(verbose_name=u'Газовий генератор', default=True,
                                     help_text=u'Для відображення на сайті необхідно виділити!')
    welding_image  = models.ImageField(verbose_name=u'Фото зварювального генератора',
                                       upload_to='products/genset/welding', blank=False)
    welding_active = models.BooleanField(verbose_name=u'Зварювальний генератор', default=True,
                                         help_text=u'Для відображення на сайті необхідно виділити!')
    equipment_image  = models.ImageField(verbose_name=u'Фото додаткового обладнання',
                                         upload_to='products/genset/equipment', blank=False)
    equipment_active = models.BooleanField(verbose_name=u'Додаткове обладнання', default=True,
                                           help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Генератори загальна'
        verbose_name_plural = u'Генератори загальна'

    def __str__(self):
        return u'Список категорій генераторів'


class GensetDiesel(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Дизель-генератор'
        verbose_name_plural = u'Дизель-генератори'

    def __str__(self):
        return self.title


def genset_diesel_upload_location(instance, filename):
    return 'products/genset_diesel/%s' % filename


class GensetDieselImage(models.Model):
    diesel     = models.ForeignKey(GensetDiesel, on_delete=models.CASCADE, related_name='genset_diesel_images')
    image      = models.ImageField(upload_to=genset_diesel_upload_location)
    active     = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                     help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.diesel.title


class GensetBenzine(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Бензиновий генератор'
        verbose_name_plural = u'Бензинові генератори'

    def __str__(self):
        return self.title


def genset_benzine_upload_location(instance, filename):
    return 'products/genset_benzine/%s' % filename


class GensetBenzineImage(models.Model):
    benzine    = models.ForeignKey(GensetBenzine, on_delete=models.CASCADE, related_name='genset_benzine_images')
    image      = models.ImageField(upload_to=genset_benzine_upload_location)
    active     = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                     help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.benzine.title


class GensetGas(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Газовий генератор'
        verbose_name_plural = u'Газові генератори'

    def __str__(self):
        return self.title


def genset_gas_upload_location(instance, filename):
    return 'products/genset_gas/%s' % filename


class GensetGasImage(models.Model):
    gas        = models.ForeignKey(GensetGas, on_delete=models.CASCADE, related_name='genset_gas_images')
    image      = models.ImageField(upload_to=genset_gas_upload_location)
    active     = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                     help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.gas.title


class GensetWelding(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Зварювальний генератор'
        verbose_name_plural = u'Зварювальні генератори'

    def __str__(self):
        return self.title


def genset_welding_upload_location(instance, filename):
    return 'products/genset_welding/%s' % filename


class GensetWeldingImage(models.Model):
    welding    = models.ForeignKey(GensetWelding, on_delete=models.CASCADE, related_name='genset_welding_images')
    image      = models.ImageField(upload_to=genset_welding_upload_location)
    active     = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                     help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.welding.title


class GensetAdditionalEquipment(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Додаткове обладнання для генератора'
        verbose_name_plural = u'Додаткове обладнання для генераторів'

    def __str__(self):
        return self.title


def genset_additional_upload_location(instance, filename):
    return 'products/genset_additional/%s' % filename


class GensetAdditionalImage(models.Model):
    additional = models.ForeignKey(GensetAdditionalEquipment, on_delete=models.CASCADE,
                                   related_name='genset_additional_images')
    image      = models.ImageField(upload_to=genset_additional_upload_location)
    active     = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                     help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.additional.title
