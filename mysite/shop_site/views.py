from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from dal import autocomplete
from django.contrib.auth.models import User
from .models import Сategory, AuthorСategory, Product, ProductMaterial
# List views


class IndexView(TemplateView):
    template_name = 'shop_site/index.html'

    def get(self, request, *args, **kwargs):
        author = get_object_or_404(User, id=self.kwargs['author'])
        kwargs.setdefault("author", author)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.kwargs['author']
        category = self.kwargs.get('category', None)
        context['auth_categories'] = AuthorСategory.objects.filter(
            author=author).all()
        if not category:
            context['products'] = Product.objects.filter(
                is_top=True, author=author)[:12]
        else:
            context['category'] = get_object_or_404(Сategory, id=category)
            context['products'] = Product.objects.filter(
                author_category__category__id=category, author=author)[:12]
        return context


# Детальный просмотр продукта
class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'

    def get_template_names(self):
        if self.object.kind == 'text_input':
            return 'shop_site/product_text_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_materials'] = ProductMaterial.objects.filter(
            product__id=self.object.id).all()
        return context


class CategotyAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Сategory.objects.all()
        if self.q:
            qs = qs.filter(title__icontains=self.q)
        return qs
