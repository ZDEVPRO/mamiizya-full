# Generated by Django 4.1.4 on 2023-01-06 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_settings', '0002_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='big_title',
            field=models.TextField(default='big'),
            preserve_default=False,
        ),
    ]
