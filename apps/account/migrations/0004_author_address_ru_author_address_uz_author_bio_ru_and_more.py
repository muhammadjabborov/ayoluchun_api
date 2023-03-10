# Generated by Django 4.1.7 on 2023-03-10 12:26

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_email_alter_user_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='address_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='author',
            name='address_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_ru',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='About author'),
        ),
        migrations.AddField(
            model_name='author',
            name='bio_uz',
            field=ckeditor.fields.RichTextField(null=True, verbose_name='About author'),
        ),
        migrations.AddField(
            model_name='author',
            name='job_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Job'),
        ),
        migrations.AddField(
            model_name='author',
            name='job_uz',
            field=models.CharField(max_length=100, null=True, verbose_name='Job'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='name_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='jobposition',
            name='name_uz',
            field=models.CharField(max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='First name'),
        ),
        migrations.AddField(
            model_name='user',
            name='first_name_uz',
            field=models.CharField(max_length=30, null=True, verbose_name='First name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name_ru',
            field=models.CharField(max_length=30, null=True, verbose_name='Last name'),
        ),
        migrations.AddField(
            model_name='user',
            name='last_name_uz',
            field=models.CharField(max_length=30, null=True, verbose_name='Last name'),
        ),
        migrations.AlterField(
            model_name='author',
            name='job',
            field=models.CharField(max_length=100, verbose_name='Job'),
        ),
    ]