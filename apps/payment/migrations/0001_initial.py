# Generated by Django 4.1.7 on 2023-03-10 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sum', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Sum')),
                ('payment_type', models.CharField(choices=[('Payme', 'Payme'), ('Apelsin', 'Apelsin'), ('Kpay', 'Kpay'), ('Click', 'Click'), ('Visa', 'Visa'), ('Mastercard', 'Mastercard')], default='Payme', max_length=25, verbose_name='Sales type')),
                ('payment_status_type', models.CharField(choices=[('Success', 'Success'), ('Failed', 'Failed'), ('Waiting', 'Waiting')], default='Waiting', max_length=25, verbose_name='Sales type')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_payments', to='course.course', verbose_name='Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_payments', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
