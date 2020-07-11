from django import forms
from .models import Сategory, Product


# Форма категории
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Сategory
        fields = ['title']


# Форма продукта
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
