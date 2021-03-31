# Generated by Django 2.2 on 2021-03-31 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='message_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_message', to='login_app.User'),
        ),
        migrations.AlterField(
            model_name='message',
            name='message_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='get_message', to='login_app.User'),
        ),
    ]
