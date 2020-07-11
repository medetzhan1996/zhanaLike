# Generated by Django 3.0.5 on 2020-07-04 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_site', '0003_auto_20200704_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_top',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='kind',
            field=models.CharField(choices=[('normal', 'Обычный'), ('image_select', 'Выбор изображения'), ('text_input', 'Набор текста')], default='normal', max_length=12),
        ),
    ]
