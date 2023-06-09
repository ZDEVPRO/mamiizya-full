# Generated by Django 4.1.7 on 2023-03-14 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sections', '0007_alter_section9to10_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section11Plus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=600)),
                ('price', models.CharField(max_length=600)),
                ('image', models.ImageField(upload_to='images/')),
                ('link', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': "Bo'lim 11+",
                'verbose_name_plural': "Bo'lim 11+",
            },
        ),
    ]
