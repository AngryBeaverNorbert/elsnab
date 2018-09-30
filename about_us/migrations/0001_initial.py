# Generated by Django 2.0.6 on 2018-09-16 12:58

import about_us.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to=about_us.models.upload_location, verbose_name='Зображення')),
                ('active', models.BooleanField(default=True, help_text='Для відображення на сайті необхідно виділити!', verbose_name='Відображати на сайті')),
            ],
            options={
                'verbose_name': 'Про нас',
                'verbose_name_plural': 'Про нас',
            },
        ),
    ]