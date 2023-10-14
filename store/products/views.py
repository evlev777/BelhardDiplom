from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from .models import Product, ProductCategory


class IndexView(TemplateView):
    template_name = 'products/index.html'
    title = 'Store'

class ProductListView(ListView):
    model = Product
    context_object_name = 'product_list'
    template_name = 'products/products.html'
    title = 'Store - Каталог'

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context
