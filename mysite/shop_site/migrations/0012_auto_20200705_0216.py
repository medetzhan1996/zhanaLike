# Generated by Django 3.0.5 on 2020-07-04 20:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0011_productmaterial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductMaterial',
            new_name='Material',
        ),
    ]