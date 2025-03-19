# Generated by Django 4.2.20 on 2025-03-19 11:22

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_alter_shortenedurl_short_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='short_code',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=30, unique=True),
        ),
    ]
