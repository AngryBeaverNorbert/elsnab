# -*- coding: utf-8 -
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.db import models


class Blog(models.Model):
    title   = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content = models.TextField(verbose_name=u'Текст', blank=False)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    class Meta:
        verbose_name        = u'Блог'
        verbose_name_plural = u'Блоги'

    def __str__(self):
        return self.title


class SingleBlog(models.Model):
    title     = models.CharField(max_length=120, verbose_name=u'Назва', blank=False)
    content   = RichTextUploadingField(verbose_name=u'Текст')
    category  = models.CharField(max_length=120, verbose_name=u'Категорія', help_text=u'Може бути пустим',
                                 blank=True, null=True)
    active    = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                    help_text=u'Для відображення на сайті необхідно виділити!')
    timestamp = models.DateField(verbose_name=u'Добавлено', auto_now_add=True)

    class Meta:
        verbose_name        = u'Стаття'
        verbose_name_plural = u'Статті'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:blog_post', kwargs={'pk': self.pk})


def blog_upload_location(instance, filename):
    return 'blog/%s' % filename


class BlogImage(models.Model):
    blog    = models.ForeignKey(SingleBlog, on_delete=models.CASCADE, related_name='blog_images')
    image   = models.ImageField(upload_to=blog_upload_location)
    active  = models.BooleanField(verbose_name=u'Відображати на сайті', default=True,
                                  help_text=u'Для відображення на сайті необхідно виділити!')

    def __unicode__(self):
        return self.blog.title
