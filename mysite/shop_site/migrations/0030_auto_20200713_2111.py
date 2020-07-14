# Generated by Django 3.0.8 on 2020-07-13 15:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_site', '0029_product_shipping_return'),
    ]

    operations = [
        migrations.AddField(
            model_name='сategory',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='author_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_category', to='shop_site.Сategory'),
        ),
    ]
