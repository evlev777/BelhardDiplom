from django.conf import settings
from django.shortcuts import HttpResponseRedirect
from django.views.generic import ListView, TemplateView
from django.contrib.auth.decorators import login_required

from .models import Product, ProductCategory, Basket


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

@login_required
def basket_add(request, product_id):
    Basket.create_or_update(user=request.user, product_id=product_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
