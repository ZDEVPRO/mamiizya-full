# Generated by Django 4.1.7 on 2023-03-08 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0007_telegrambot'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='telegrambot',
            options={'verbose_name': 'Telegram Bot', 'verbose_name_plural': 'Telegram Bot'},
        ),
    ]
