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

    def dispatch(self, *args, **kwargs):
        self.auth_categories = Сategory.objects.filter(
            author=self.request.user.id).all()
        self.products = Product.objects.filter(
            is_top=True, author=self.request.user.id)[:12]
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        product = None
        if request.is_ajax():
            product = get_object_or_404(
                Product, id=request.GET.get('product_id'))
            return render(request, 'manager/product_modal.html',
                          {'product_form': self.product_form_class(
                              instance=product), 'product': product})
        return self.render_to_response(
            {
                'category_form': self.category_form_class(),
                'product_form': self.product_form_class(),
                'auth_categories': self.auth_categories,
                'products': self.products,
                'product': product
            })

    def post(self, request, *args, **kwargs):
        form_args = {
            'data': self.request.POST
        }
        if request.POST.get('category-submit', None):
            category_form = self.category_form_class(**form_args)
            if category_form.is_valid():
                category_form.save()
        elif request.POST.get('product-submit', None):
            product_id = request.POST.get('product_id', None)
            if product_id:
                product = get_object_or_404(
                    Product, id=request.POST.get('product_id'))
                product_form = self.product_form_class(
                    request.POST, request.FILES, instance=product)
            else:
                product_form = self.product_form_class(
                    request.POST, request.FILES)
            if product_form.is_valid():
                product_form.save()
            else:
                print(product_form.errors)
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
