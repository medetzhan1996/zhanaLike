# Generated by Django 3.0.8 on 2020-07-07 21:35

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0027_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='details',
            field=tinymce.models.HTMLField(blank=True, null=True),
        ),
    ]
