# Generated by Django 3.0.8 on 2020-07-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0023_auto_20200707_0233'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='file_extra1',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='file_extra2',
            field=models.FileField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='file_extra3',
            field=models.FileField(null=True, upload_to='images'),
        ),
    ]
