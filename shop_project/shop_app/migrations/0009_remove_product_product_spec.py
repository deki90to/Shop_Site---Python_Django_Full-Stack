# Generated by Django 3.1.5 on 2021-01-11 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0008_auto_20210111_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_spec',
        ),
    ]