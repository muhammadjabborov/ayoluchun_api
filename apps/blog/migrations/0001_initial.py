# Generated by Django 4.1.7 on 2023-03-08 22:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import thumbnails.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('icon', thumbnails.fields.ImageField(upload_to='icons/Y%/m%/%d/')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Category Model',
                'verbose_name_plural': 'Category',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('device_id', models.CharField(max_length=100)),
                ('views', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(unique=True, verbose_name='Slug')),
                ('photo', thumbnails.fields.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo')),
                ('get_thumbnails', thumbnails.fields.ImageField(upload_to='')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Author', to='account.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Category', to='blog.category')),
            ],
            options={
                'verbose_name': 'Blog Model',
                'verbose_name_plural': 'Blog',
                'ordering': ['-created_at'],
            },
        ),
    ]