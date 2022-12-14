# Generated by Django 4.1 on 2022-09-28 10:20

from django.db import migrations, models
import entries.models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0002_entry_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(help_text='Add a comment', max_length=120),
        ),
        migrations.AlterField(
            model_name='entry',
            name='images',
            field=models.ImageField(blank=True, upload_to=entries.models.upload_to_directory),
        ),
    ]
