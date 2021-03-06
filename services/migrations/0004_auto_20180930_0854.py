# Generated by Django 2.0.6 on 2018-09-30 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_singleservice_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='singleinstallation',
            name='category',
            field=models.CharField(blank=True, help_text='Може бути пустим', max_length=120, null=True, verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='singleinstallation',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Добавлено'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singlemontage',
            name='category',
            field=models.CharField(blank=True, help_text='Може бути пустим', max_length=120, null=True, verbose_name='Категорія'),
        ),
        migrations.AddField(
            model_name='singlemontage',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Добавлено'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='singleservice',
            name='timestamp',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Добавлено'),
            preserve_default=False,
        ),
    ]
