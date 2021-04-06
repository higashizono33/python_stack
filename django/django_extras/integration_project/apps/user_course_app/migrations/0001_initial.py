# Generated by Django 2.2 on 2021-04-01 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0002_auto_20210320_1809'),
        ('courses_app', '0003_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses_app.Course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.Users')),
            ],
        ),
    ]