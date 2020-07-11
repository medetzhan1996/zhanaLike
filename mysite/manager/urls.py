from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'manager'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.IndexView.as_view(), name='index'),
    path('product/<int:id>', views.ProductDetailView.as_view(),
         name='product_detail'),
]
