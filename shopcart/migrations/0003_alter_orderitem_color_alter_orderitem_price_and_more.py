# Generated by Django 4.1.7 on 2023-03-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0002_alter_orderitem_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='color',
            field=models.CharField(max_length=600, verbose_name='Rangi'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.CharField(max_length=600, verbose_name='Narxi'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(verbose_name='Miqdori'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='size',
            field=models.CharField(max_length=600, verbose_name="O'lchami"),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='title',
            field=models.CharField(max_length=600, verbose_name='Nomi'),
        ),
    ]