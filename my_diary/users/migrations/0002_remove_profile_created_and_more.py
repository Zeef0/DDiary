# Generated by Django 4.1 on 2022-09-11 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='created',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='following_user_id',
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
