# Generated by Django 3.1.2 on 2021-02-13 22:50

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0014_auto_20210213_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='productname',
            name='ad_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[200, 110], upload_to='pictures'),
        ),
        migrations.AlterField(
            model_name='productname',
            name='product_picture_1',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=100, size=[1920, 1080], upload_to='pictures'),
        ),
    ]
