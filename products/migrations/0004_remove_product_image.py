# Generated by Django 3.0.5 on 2020-04-16 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
