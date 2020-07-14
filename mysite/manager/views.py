from django.shortcuts import redirect, render
from django.views.generic.base import TemplateResponseMixin, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from shop_site.models import Product, Сategory
from shop_site.forms import CategoryForm, ProductForm


# Главная страница менеджера
class IndexView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'manager/index.html'
    category_form_class = CategoryForm
    product_form_class = ProductForm
    auth_categories = None
    products = None
    product = None
    category = None

    def dispatch(self, *args, **kwargs):
        self.categories = Сategory.objects.filter(
            author=self.request.user.id).all()
        self.products = Product.objects.filter(
            is_top=True, author=self.request.user.id)[:12]
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            if request.GET.get('product_edit', None):
                self.product = get_object_or_404(
                    Product, id=request.GET.get('product_id'))
                return render(request, 'manager/product_modal.html',
                              {'product_form': self.product_form_class(
                                  instance=self.product),
                               'product': self.product})
            elif request.GET.get('category_edit', None):
                self.category = get_object_or_404(
                    Сategory, id=request.GET.get('category_id'))
                return render(request, 'manager/category_modal.html',
                              {'category_form': self.category_form_class(
                                  instance=self.category),
                               'category': self.category})
            elif request.GET.get('category_remove', None):
                self.category = get_object_or_404(
                    Сategory, id=request.GET.get('category_id'))
                return render(request, 'manager/category_remove_modal.html',
                              {'category': self.category})
            elif request.GET.get('product_remove', None):
                self.product = get_object_or_404(
                    Product, id=request.GET.get('product_id'))
                return render(request, 'manager/product_remove_modal.html',
                              {'product': self.product})
        return self.render_to_response(
            {
                'category_form': self.category_form_class(),
                'product_form': self.product_form_class(),
                'categories': self.categories,
                'products': self.products,
                'product': self.product,
                'category': self.category
            })

    def post(self, request, *args, **kwargs):
        if request.POST.get('category-submit', None):
            category_id = request.POST.get('category_id', None)
            if category_id:
                category = get_object_or_404(Сategory, id=category_id)
                category_form = self.category_form_class(
                    request.POST, instance=category)
            else:
                category_form = self.category_form_class(request.POST)
            if category_form.is_valid():
                category_form.save()
        elif request.POST.get('product-submit', None):
            product_id = request.POST.get('product_id', None)
            if product_id:
                product = get_object_or_404(Product, id=product_id)
                product_form = self.product_form_class(
                    request.POST, request.FILES, instance=product)
            else:
                product_form = self.product_form_class(
                    request.POST, request.FILES)
            if product_form.is_valid():
                product_form.save()
            else:
                print(product_form.errors)
        elif request.POST.get('category-remove-submit', None):
            Сategory.objects.filter(id=request.POST.get(
                'category_id'), author=request.user.id).delete()
        elif request.POST.get('product-remove-submit', None):
            Сategory.objects.filter(id=request.POST.get(
                'product_id'), author=request.user.id).delete()
        return redirect('manager:index')


# Главная страница менеджера
class ProductDetailView(LoginRequiredMixin, TemplateResponseMixin, View):
    template_name = 'manager/product_text_detail.html'
    product_form_class = ProductForm
    products = None

    def dispatch(self, *args, **kwargs):
        self.product = get_object_or_404(Product, id=self.kwargs['id'])
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return self.render_to_response(
            {
                'product': self.product,
                'product_form': self.product_form_class(instance=self.product)
            })

    def post(self, request, *args, **kwargs):
        product_form = self.product_form_class(
            request.POST, request.FILES, instance=self.product)
        if product_form.is_valid():
            product_form.save()
            return redirect('manager:index')
        return self.render_to_response({'product': self.product,
                                        'product_form': product_form})
