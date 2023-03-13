# Generated by Django 4.1.7 on 2023-03-13 11:13

import ckeditor.fields
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('photo', models.ImageField(upload_to='advertisement/%Y/%m/%d/', verbose_name='Photo')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('link', models.CharField(max_length=255, verbose_name='Link')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
            ],
            options={
                'verbose_name': 'Advertisement',
                'verbose_name_plural': 'Advertisements',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Elektron pochta')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('address_uz', models.CharField(max_length=255, null=True, verbose_name='Address')),
                ('address_ru', models.CharField(max_length=255, null=True, verbose_name='Address')),
                ('map', models.CharField(max_length=255, verbose_name='Map')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Elektron pochta')),
                ('msg', models.TextField(verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('photo', models.ImageField(upload_to='course/photo/%Y/%m/%d/', verbose_name='Photo')),
                ('context', ckeditor.fields.RichTextField(verbose_name='Context')),
                ('context_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Context')),
                ('context_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Context')),
            ],
            options={
                'verbose_name': 'Notification',
                'verbose_name_plural': 'Notifications',
            },
        ),
        migrations.CreateModel(
            name='RulesOfUse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('description_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
                ('description_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'RulesOfUse',
                'verbose_name_plural': 'RulesOfUses',
            },
        ),
    ]
