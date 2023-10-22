from django.urls import path
from .views import IndexView, ProductListView, basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('catalog/', ProductListView.as_view(), name='catalog'),
    path('page/<int:page>/', ProductListView.as_view(), name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='category')
]