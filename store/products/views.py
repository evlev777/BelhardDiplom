from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Product, ProductCategory


class IndexView(TemplateView):
    template_name = 'products/index.html'
    title = 'Store'

class ProductListView(ListView):
    model = Product
    queryset = model.objects.all()
    context_object_name = 'product_list'
    template_name = 'products/products.html'
    title = 'Store - Каталог'

