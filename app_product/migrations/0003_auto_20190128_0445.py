# Generated by Django 2.0.8 on 2019-01-28 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_product', '0002_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(upload_to='products'),
        ),
    ]
