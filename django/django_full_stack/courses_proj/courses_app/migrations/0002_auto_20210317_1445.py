# Generated by Django 2.2 on 2021-03-17 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='description',
            old_name='description',
            new_name='content',
        ),
    ]
