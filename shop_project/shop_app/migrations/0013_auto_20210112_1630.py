# Generated by Django 3.1.2 on 2021-01-12 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0012_auto_20210112_1626'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='category_name',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='category_name',
            new_name='product_type',
        ),
    ]
