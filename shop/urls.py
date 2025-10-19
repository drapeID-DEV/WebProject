from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='products'),
    path('create', views.createProduct, name='create'),
    path('<int:pk>', views.ProductDetailView.as_view(),  name='product-detail'),
    path('update/<int:pk>', views.ProductUpdateView.as_view(),  name='product-update'),
    path('delete/<int:pk>', views.ProductDeletelView.as_view(),  name='product-delete'),
]
