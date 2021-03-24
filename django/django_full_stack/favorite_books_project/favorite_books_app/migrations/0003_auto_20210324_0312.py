# Generated by Django 2.2 on 2021-03-24 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favorite_books_app', '0002_auto_20210324_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='books',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='books',
            name='users_who_like',
            field=models.ManyToManyField(related_name='liked_books', to='login_app.Users'),
        ),
    ]
