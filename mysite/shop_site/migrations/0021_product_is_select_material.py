# Generated by Django 3.0.5 on 2020-07-04 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0020_auto_20200705_0405'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_select_material',
            field=models.BooleanField(default=False),
        ),
    ]