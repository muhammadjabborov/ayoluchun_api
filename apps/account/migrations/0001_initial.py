# Generated by Django 4.1.7 on 2023-03-10 12:53

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=60, null=True, unique=True, verbose_name='Elektron pochta')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='Username')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='Phone')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('first_name_uz', models.CharField(max_length=30, null=True, verbose_name='First name')),
                ('first_name_ru', models.CharField(max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('last_name_uz', models.CharField(max_length=30, null=True, verbose_name='Last name')),
                ('last_name_ru', models.CharField(max_length=30, null=True, verbose_name='Last name')),
                ('birthday', models.DateTimeField(blank=True, null=True, verbose_name='Birthday')),
                ('gender', models.CharField(choices=[('Erkak', 'Male'), ('Ayol', 'Female')], default='Ayol', max_length=15)),
                ('is_gmail_active', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='oxirgi kirish')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=255, null=True, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Job Position',
                'verbose_name_plural': 'Job Positions',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='user.png', null=True, upload_to='authors', verbose_name='Photo')),
                ('post_code', models.IntegerField(default=0, verbose_name='Post code')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('address_uz', models.CharField(max_length=255, null=True, verbose_name='Address')),
                ('address_ru', models.CharField(max_length=255, null=True, verbose_name='Address')),
                ('instagram', models.CharField(max_length=255, verbose_name='Instagram')),
                ('imkon', models.CharField(max_length=255, verbose_name='Imkon')),
                ('linkedin', models.CharField(max_length=255, verbose_name='Linkedin')),
                ('job', models.CharField(max_length=100, verbose_name='Job')),
                ('job_uz', models.CharField(max_length=100, null=True, verbose_name='Job')),
                ('job_ru', models.CharField(max_length=100, null=True, verbose_name='Job')),
                ('bio', ckeditor.fields.RichTextField(null=True, verbose_name='About author')),
                ('bio_uz', ckeditor.fields.RichTextField(null=True, verbose_name='About author')),
                ('bio_ru', ckeditor.fields.RichTextField(null=True, verbose_name='About author')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.jobposition', verbose_name='Job Position')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.region', verbose_name='Region')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
    ]
