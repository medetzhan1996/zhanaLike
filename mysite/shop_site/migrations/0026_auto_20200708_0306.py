# Generated by Django 3.0.8 on 2020-07-07 21:06

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0025_auto_20200707_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
