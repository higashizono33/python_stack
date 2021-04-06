# Generated by Django 2.2 on 2021-03-23 03:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0002_auto_20210320_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='birthday',
        ),
        migrations.AlterField(
            model_name='users',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]