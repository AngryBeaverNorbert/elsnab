# Generated by Django 2.0.6 on 2018-09-30 10:49

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Назва')),
                ('content', models.TextField(verbose_name='Текст')),
                ('active', models.BooleanField(default=True, help_text='Для відображення на сайті необхідно виділити!', verbose_name='Відображати на сайті')),
            ],
            options={
                'verbose_name_plural': 'Блоги',
                'verbose_name': 'Блог',
            },
        ),
        migrations.CreateModel(
            name='BlogImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=blog.models.blog_upload_location)),
                ('active', models.BooleanField(default=True, help_text='Для відображення на сайті необхідно виділити!', verbose_name='Відображати на сайті')),
            ],
        ),
        migrations.CreateModel(
            name='SingleBlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='Назва')),
                ('category', models.CharField(blank=True, help_text='Може бути пустим', max_length=120, null=True, verbose_name='Категорія')),
                ('active', models.BooleanField(default=True, help_text='Для відображення на сайті необхідно виділити!', verbose_name='Відображати на сайті')),
                ('timestamp', models.DateField(auto_now_add=True, verbose_name='Добавлено')),
            ],
            options={
                'verbose_name_plural': 'Блоги (детальні)',
                'verbose_name': 'Блог (детальний)',
            },
        ),
        migrations.AddField(
            model_name='blogimage',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_images', to='blog.SingleBlog'),
        ),
    ]
