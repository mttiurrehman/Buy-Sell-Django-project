# Generated by Django 4.0 on 2022-08-16 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_product_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image',
        ),
    ]
