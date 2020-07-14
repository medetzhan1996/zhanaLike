from django.contrib import admin
from .models import Сategory, Product, ProductMaterial, Material

# Cписок моделей администрации
admin.site.register(Сategory)
admin.site.register(Product)
admin.site.register(ProductMaterial)
admin.site.register(Material)
