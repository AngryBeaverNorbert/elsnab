# Generated by Django 2.0.6 on 2018-09-16 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180916_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=254, verbose_name='Заголовок')),
                ('body', models.TextField(verbose_name='Тіло')),
            ],
            options={
                'verbose_name': 'Домашня сторінка',
                'verbose_name_plural': 'Домашні сторінки',
            },
        ),
        migrations.DeleteModel(
            name='HomeView',
        ),
    ]